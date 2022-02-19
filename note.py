import datetime
import math
import os
import re
import shutil
import util
from os.path import exists

content_types = ['folders', 'files']
target_extension = ".md"

def run(config, option):
    global base_directory
    global current_directory
    global exclusion_folders
    global max_cols
    global source_directory
    base_directory = config['working_directory']
    current_directory = config['working_directory']
    exclusion_folders = option['ignore']
    max_cols = int(option['max_cols'])
    source_directory = config['source_directory']

    for classification in option['classifications']:
        print(f"\r\nSelect or enter a {classification}:")
        folder_item = get_folder_item(content_types[0])
        current_directory = f"{current_directory}/{folder_item}"
        if not os.path.isdir(current_directory):
            os.mkdir(current_directory)

    template = get_template(current_directory, option['templates'])
    print(f"\r\nSelect or enter a note title:")
    file_name = get_folder_item(content_types[1])
    src_path = os.path.join(source_directory, "templates", template['file'])
    dst_path = os.path.join(current_directory, f"{file_name}{target_extension}")

    if exists(src_path):
        intrinsic_keys = ["title", "datetime"]
        variables = get_template_variables(src_path)
        for variable in variables:
            if list(variable)[0] == intrinsic_keys[0]:
                variable[intrinsic_keys[0]] = file_name
            elif list(variable)[0] == intrinsic_keys[1]:
                variable[intrinsic_keys[1]] = str(datetime.datetime.now())
        for variable in variables:
            key = list(variable)[0]
            default = variable[list(variable)[0]]
            if key not in intrinsic_keys:
                caption = f"Enter value for {key}"
                if default != '':
                    caption = f"{caption} [{default}]"
                variable[list(variable)[0]] = input(f"{caption}: ") or default

        if not exists(dst_path):
            src_file = open(src_path, "r")
            dst_file = open(dst_path, "a")
            template_lines = src_file.readlines()
            for line in template_lines:
                line = replace_variables(line, variables)
                dst_file.writelines(line)
            src_file.close()
            dst_file.close()
        else:
            src_file = open(src_path, "r")
            dst_file = open(dst_path, "a")
            delimiter = "- - -\n"
            append_text = None
            while True:
                line = src_file.readline()
                if line == delimiter:
                    append_text = "\n"
                if not line:
                    break 
                elif append_text is not None:
                    line = replace_variables(line, variables)                
                    append_text = f"{append_text}{line}"
            dst_file.write(append_text or '')
            src_file.close()
            dst_file.close()
    return dst_path

def  get_folder_item(content_type):
    items = os.listdir(path=current_directory)
    items.sort()
    listings = []
    for item in items:
        if content_type == content_types[0] and is_valid_folder(item):
            listings.append(item)
        elif content_type == content_types[1] and is_valid_file(item):
            listings.append(os.path.splitext(item)[0])
    formatted_listings = format_listings(listings)
    
    for listing in formatted_listings:
        print(listing)
    caption = "Selection: "
    if len(formatted_listings) == 0:
        caption = ""
    entry = input(caption)
    
    if entry.isnumeric():
        return listings[int(entry)-1]
    else:
        while not is_valid_folder(entry):
            util.reset_entry(caption)
            entry = input(f"{caption}: ")
        return entry

def is_valid_folder(item):
    current_path = f"{current_directory}/{item}"
    for folder in exclusion_folders:
        if f"{base_directory}/{folder}" in current_path:
            return False
    return re.match("^[A-Za-z0-9_-]*$", item.replace(' ', ''))

def is_valid_file(item):
    return os.path.isfile(f"{current_directory}/{item}") and get_extension(item) == target_extension

def get_extension(file):
    split_tup = os.path.splitext(file)
    return split_tup[1]

def format_listings(listings):
    min_count = 5
    result = []
    if len(listings) <= min_count:
        index = 1
        for listing in listings:
            result.append(f"  {index}) {listing}")
            index = index + 1
    else:
        row_count = math.ceil(len(listings) / max_cols)
        result = [""] * row_count
        size = os.get_terminal_size()
        col_width = math.floor(size.columns/max_cols)
        list_queue = listings.copy()
        listing_index = 0
        while len(list_queue) > 0:
            for row_index in range(row_count):
                if len(list_queue) > 0:
                    listing_index = listing_index + 1
                    listing_index_width = 5
                    listing = f"{listing_index}) ".rjust(listing_index_width)
                    listing = f"{listing}{list_queue.pop(0)}"
                    if len(listing) >= col_width:
                        listing = f"{listing[0:col_width-listing_index_width]}..."
                    listing = listing.ljust(col_width)
                    result[row_index] = f"{result[row_index]}{listing}"
    return result

def get_template(path, templates):
    new_path = path.replace(base_directory, "")
    paths = []
    result = None
    for template in templates:
        if 'target_paths' in template.keys():
            for path in template['target_paths']:
                if new_path[0:len(path)] == path:
                    paths.append(path)
                    break
    longest_path = ''
    for path in paths:
        if len(path) > len(longest_path):
            longest_path = path
    for template in templates:
        if 'target_paths' in template.keys() and longest_path in template['target_paths']:
            result = template
            break
    if result is None:
        result = {
            "template": "_default.md"
        }
    return result

def replace_variables(line, variables):
    for variable in variables:
        key = list(variable)[0]
        key_regex = r"\{(" + key + ".*?)\}"
        value = variable[list(variable)[0]]
        if key == "amount":
            line = re.sub(key_regex, value, line)
        else:
            line = line.replace(f"{{{key}}}", str(value or ''))
    return line

def create_scratchpad(config):
    dst_filename = "Scratchpad.md"
    dst_file = os.path.join(config['working_directory'], dst_filename)
    if not exists(dst_file):
        src_filename = "_scratchpad.md"
        src_file = os.path.join(config['source_directory'], "templates", src_filename)
        shutil.copyfile(src_file, dst_file)

def get_template_variables(src_path):
    variables = []
    var_regex = r"\{(.*?)\}"
    delimiter = '='

    with open(src_path, "r") as src_file:
        template_lines = src_file.readlines()
        for line in template_lines:
            vars = re.findall(var_regex, line)
            for var in vars:
                if delimiter not in var:
                    var = f"{var}="
                name = var[0:var.index(delimiter)]
                value = var[var.index(delimiter)+1:]
                var_exists = False
                for variable in variables:
                    if list(variable)[0] == name:
                        var_exists = True
                        break
                if not var_exists:
                    variables.append({name: value})
    return variables