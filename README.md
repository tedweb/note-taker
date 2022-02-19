# Scribe

##### *Do you take lots of notes? Are they scattered across multiple files, folders and apps?*

##### *Do you ever have the need to quickly create a note in a matter of seconds?*

##### *Tired of navigating various apps, browsers and tabs just to locate that one note to add a comment?*

In today's work-from-anywhere world, keeping everything organized can be a challenge. Scribe works to simplify one aspect of your everyday work life... your daily notes. You take them. You need them. Let's organize them! Scribe follows the '*Less Is More*' mentality. No GUI interface, just a simple command line that can be launched from an icon on your desktop.

###### <img src="./resources/scribe_giphy.gif" style="zoom:100%;border: 1px solid gray;">

1. [Overview](#overview)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Operation](#operation)
5. [Templates](#templates)
6. [Variables](#variables)
7. [Configuration](#configuration)

- - -

#### Overview

[Back to Top](#scribe)

**Save brain cycles for the important stuff, rely on muscle memory for the repetitive stuff!**

In today's age of information, we're constantly jumping from one meeting to the next. On average, using a GUI based tool can waste valuable time during the most crucial part of a meeting. Scribe users can generate a pre-formatted note in less than 10 seconds!

**No more reading between the lines.**

Chances are, you take different types of notes. One for learning, one for deal opportunities, one for your weekly meal plan. These various types of notes require their own unique format. Properly formatting them to meet their content type is needed for meaningfulness. Scribe automatically detects what type of note you're taking and pre-formats it using smart-templates!

**What's so smart about your templates?**

It varies... literally. Scribe templates support variables. This means you can be prompted for key details before your note is even created! Once defined, these variables will be plugged into your note and ready for your review!

**Consistency is the key to a note-worthy work-style.**

Do you want to hide your notes in obscure places so you'll never find them? If so, there are plenty of offerings out there that can do just that. But not Scribe. By default, folders are limited to only two levels of nesting. This limitation is by design and allows for easier reference once saved. Don't like that? Configure it your way to meet your style.

**Some other things to consider:**

* Compatible with Windows, Linux and MacOS
* This utility simply creates [markdown](https://en.wikipedia.org/wiki/Markdown) files one the fly... it is NOT a markdown editor.  We have some amazing recommendations in the [Requirements](#requirements) section. If you have any suggestions feel free to email me. I'll be happy to review and consider adding it to my list.
* The first time Scribe runs, it will prompt you to enter the location of where you wish to keep your notes.  Make sure this folder alreday exists beforehand.

- - -

#### Requirements

[Back to Top](#scribe)

This utility is a Python3 script.  Make sure the following requirements have been installed:

* [Python3](https://www.python.org/downloads/)
* [PyYAML](https://pyyaml.org/)

A WYSIWYG markdown editor is highly recommended.  Below are two worth considering:

> ##### <img src="./resources/typora.png" style="width:80px;"> [Typora](https://typora.io/)
> 
> This little app is available on Windows, Mac and Linux. The interface is minimalistic with no toolbar to clutter your screen. All text formatting is driven by menu options or keyboard shortcuts. This may sound intimidating at first, but after spending 10-15 minutes with it you'll be editing markdown notes effortlessly in no time.
> 
> Price: $14.99 with 14 day trial.

> ##### <img src="./resources/unotes.png" style="width:80px;"> [UNotes](https://marketplace.visualstudio.com/items?itemName=ryanmcalister.Unotes)
> 
> This is a plugin for VS Code. If you're a developer looking for a better way to edit your README files, give UNotes a try. The interface is intuitive and has nice features like inline embedding of images.
> 
> Price: FREE!

- - -

#### Installation

[Back to Top](#scribe)

This is a command line interface (CLI) tool.  CLIs offer the ability to do repetitive tasks more efficiently and faster than a GUI interface because there's only a single device to interact with, the keyboard. Nonetheless, users must be familiar with their operating system's [terminal](https://itconnect.uw.edu/learn/workshops/online-tutorials/web-publishing/what-is-a-terminal/) app. VS Code users can run this utility app directy from the IDE's built in terminal pane for a unified system of engagement. To install, make sure Python3 and PyYAML is installed (noted above) then follow the below 3-step process:

1. Navigate to the directory of your choice from your terminal app. An example would be:
`cd /Users/jsmith/Documents/Projects`
2. Run the following GIT command:
`git clone https://github.com/tedweb/scribe.git`
This will download the project file into the directory from step one. The output should read similar to this:![image](./resources/git_clone.png)
3. Scribe is now operational. Run the following command to execute:
`python3 scribe.py`

**Special Note:** The first run will prompt you to enter the path of where you would like to keep your notes. It is strongly recommended to keep notes in a seprate folder away from where Scribe is installed. I personally prefer to keep them in a folder called 'Notes' within my 'Documents' folder.

**Desktop Shortcuts:** Desktop shortcuts offer an easy way to launch Scribe. However, the process of creating shortcuts can vary depending which operating system you are using (Mac, Linux or Windows), it's simply a matter of run-in command from a scriptable file:

`python3 ~/Documents/Projects/Scribe/scribe.py`

- - -

#### Operation

Running the command mentioned above will prompt you with a set of questions. Primarily, which folder to keep your note and what do you want to call your note. By default, folders are managed in a unified two level classification (categories & groups). This is by design to keep navigation in a consistent fashion which is key to simplifying repetitive tasks. Classifications can be changed to your liking within the config file.

###### <img src="./resources/Screenshot.png" style="zoom:100%;">

At this point, your note has been created! You are now ready to start using the WYSIWYG editor of your choice to append and edit your notes!

Here's a screenshot of the Typora interface.

###### <img src="./resources/widgets_note.png" style="zoom:75%;">

Here's a screenshot of the UNotes + VSCode interface.

###### <img src="./resources/vscode.png" style="zoom:75%;">

- - -

#### Templates

Templates can be used to apply customized formats to your notes. Create and save templates in markdown format with an extension of '.md' within the 'templates' folder. Templates must be references within the config.yml file with the following attributes:

- file: The name of the template file within the 'templates' folder.
- target_paths: A list of file paths within your notes directory to determine which template is applied.

###### ![image-20220216114253258](./resources/template.png)

In the screenshot above, the 'opportunity.md' template will be applied to notes created in the FY21, FY22, FY23 sub-folders of the notes directory.

- - -

#### Variables

Templates can contain variables with values that will be defined when the note is created.  To create a variable within a template, wrap varible name within curly braces:

###### ![image-20220216115230336](resources/variable_undefined.png)

The sample template above has four declared variables:

- title
- datetime
- main course
- sides

Scribe will prompt user to define these variables during note creation:

###### ![image-20220216115230336](resources/scribe_variable_defining.png)

Note: 'title' and 'datetime' are reserved variable names that can't be overwritten.  Therefore, Scribe will not be prompt user to enter these values. Once these values have been entered from the command line, the note will have all variables replaced with those values.

###### ![image-20220216115230336](resources/variable_defined.png)

------

#### Variables with Default Values

To give a variable a default value, seperate the variable name from the default value with an equal '=' sign:

`{amount=0.00}`

Variables with default values are denoted by square brackets:

###### ![image-20220216115230336](resources/default_values.png)

Simply press the 'Enter' button to accept the default value, or override it with your own value.

------

#### Auto Launch WYSIWYG Editor

Some editors, such as Typora, support opening a specified file from the command line. To have Scribe automatically open a newly created or appended note within Typora, follow the following two steps:

1. 
2. Edit the 'post_script' attribute of the config.yml file with the following command:
   `open '{file}' -a typora`

- - -

#### Configuration

[Back to Top](#scribe)

The `config.yml` file is a YAML file allowing for customizations of the app. Current customization features include:

* `ignore`: Folders to ignore and prevent from displaying.
* `working_directory`: Where your note files are kept.
* `classifications`: This defines the unifying folder structure to organize your notes
* `template`: Custom templates can be created and assigned to specific directories within your notes folder.
* `post_script`: 