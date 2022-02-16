# Scribe

Scribe is an automated markdown generator written in Python. This utility leverages templates to provide the ability to generate and organize markdown notes directly from the command line in a matter of seconds.  Avoid frustratingly slow IDE editors and their cumbersome GUI interfaces. Fully customizable templates allows you to create pre-formatted notes quickly and easily!

<img src="./resources/scribe_giphy.gif" style="zoom:100%;border: 1px solid gray;" /><br>

1. [Overview](#overview)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Configuration](#configuration)

- - -

#### Overview

[Back to Top](#scribe)

* Compatible with Windows, Linux and MacOS
* This Python3 utility simply creates [markdown](https://en.wikipedia.org/wiki/Markdown) files one the fly... it is NOT a markdown editor.  The [Requirements](#requirements) section has some third party WYSIWYG recommendations.  If you have any suggestions feel free to email them to me.  I'll be happy to review and consider adding it to my list.
* Following the '*Less Is More*' way of thinking, Scribe limits folder nesting to two levels.  This can be changed through the config file by updating the 'classifications' setting.
* The first time Scribe runs, it will prompt you for where you wish to create your notes.  Make sure this folder alreday exists beforehand.

- - -

#### Requirements

[Back to Top](#scribe)

This utility is a Python3 script.  Make sure the following requirements have bene installed"

* [Python3](https://www.python.org/downloads/)
* [PyYAML](https://pyyaml.org/)

A WYSIWYG markdown editor is highly recommended.  Below are two worth considering:

> ##### <img src="./resources/typora.png" style="zoom:50%;" /> [Typora](https://typora.io/)
>
> This little app is available on Windows, Mac and Linux. The interface is minimalistic with no toolbar toolbar to clutter your screen.  This means all formatting options are driven by menu options or keyboard shortcuts.  This may sound  intimidating, at first, but after spending 10-15 minutes with it you'll be formatting your markdown notes in no time.
> Price: $14.99 with 14 day trial.

> ##### <img src="./resources/unotes.png" style="zoom:50%;" /> [UNotes](https://marketplace.visualstudio.com/items?itemName=ryanmcalister.Unotes)
>
> This is a plugin for VS Code.  If you're a developer looking for a better way to manager you README for your GIT projects, give UNotes a try.  The interface is inutitive and has nice features like inline embedding of images.  However, there are some minor shortcomings that might make it cumbersome to use.
> Price: FREE!

- - -

#### Installation

[Back to Top](#scribe)

This is a command line interface.  To install, become familiar with your operating system's [terminal](https://itconnect.uw.edu/learn/workshops/online-tutorials/web-publishing/what-is-a-terminal/) app.
Run terminal, navigate to the install directory of your choice (ex. '<span class="colour" style="color:rgb(206, 145, 120)">/Users/jsmith/Documents/Projects</span>') and run the following GIT command:
`git clone https://github.com/tedweb/scribe.git`

###### ![image](https://raw.githubusercontent.com/tedweb/scribe/main/resources/git_clone.png)

Once the code has been downloaded, run the following command to execute:
`python3 scribe.py`

Alternatively, a safer method would include the path.  Using the path example from above:
`python3 ~/Documents/Projects/Scribe/scribe.py`

The first run will prompt you to enter the path to your notes folder (ex. '<span class="colour" style="color:rgb(206, 145, 120)">/Users/jsmith/Documents/Notes</span>'). If this folder does not exist, create it. 

###### <img src="./resources/Screenshot.png" style="zoom:100%;" />

Once created, you are ready to start creating some markdown notes using the WYSIWYG editor of your choice!

Here's a screenshot of the Typora interface.

###### <img src="./resources/widgets_note.png" style="zoom:75%;" />



Here's a screenshot of the UNotes + VSCode interface.

###### <img src="./resources/vscode.png" style="zoom:75%;" />

- - -

#### Configuration

[Back to Top](#scribe)

The `config.yml` file is a YAML file allowing for customizations of the app.  Current customization features include:

* `ignore`: Folders to ignore and prevent from displaying.
* `working` directory: There your note files are kept.
* `template`: Custom templates can be created and assigned to specific directories within your notes folder.