import datetime
import math
import os
import re
import util
from os.path import exists

content_types = ['folders', 'files']
target_extension = ".md"

def run(config):
    global base_directory
    global current_directory
    global exclusion_folders
    global max_cols
    global source_directory
    base_directory = config['working_directory']
    current_directory = config['working_directory']
    exclusion_folders = config['note_exclusion_folders']
    max_cols = int(config['max_cols'])
    source_directory = config['source_directory']

    for classification in config['classifications']:
        print(f"\r\nSelect or enter a {classification}:")
        folder_item = get_folder_item(content_types[0])
        current_directory = f"{current_directory}/{folder_item}"
        if not os.path.isdir(current_directory):
            os.mkdir(current_directory)

    template = get_template(current_directory, config['templates'])
    print(f"\r\nSelect or enter a note title:")
    file_name = get_folder_item(content_types[1])
    target_file = f"{current_directory}/{file_name}{target_extension}"

    tokens = {}
    for token in template['tokens']:
        tokens[token] = None
    tokens['title'] = file_name
    tokens['datetime'] = str(datetime.datetime.now())

    if not exists(target_file):
        dest_file = open(target_file, "a")
        read_file = open(f"{source_directory}/{template['template']}", "r")
        template_lines = read_file.readlines()
        for line in template_lines:
            line = replace_tokens(line, tokens)
            dest_file.writelines(line)
        read_file.close()
        dest_file.close()

    else:
        delimiter = "- - -\n"
        append_text = None
        read_file = open(template['template'], "r")
        while True:
            line = read_file.readline()
            if line == delimiter:
                append_text = "\n"
            if not line:
                break 
            elif append_text is not None:
                line = replace_tokens(line, tokens)                
                append_text = f"{append_text}{line}\r\n"
        read_file.close()

        if append_text is not None:
            write_file = open(target_file, "a")
            write_file.write(append_text)
            write_file.close()

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
        if 'paths' in template.keys():
            for path in template['paths']:
                if new_path[0:len(path)] == path:
                    paths.append(path)
                    break
    longest_path = ''
    for path in paths:
        if len(path) > len(longest_path):
            longest_path = path
    for template in templates:
        if 'paths' in template.keys() and longest_path in template['paths']:
            result = template
            break
    if result is None:
        for template in templates:
            if 'template' in template.keys() and '_default' in template['template']:
                result = template
                break
    return result

def replace_tokens(line, tokens):
    for token,value in tokens.items():
        line = line.replace(f"{{{token}}}", value)
    return line
