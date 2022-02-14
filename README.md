# Scribe

Scribe is an automated markdown generator written in Python. This utility leverages templates to provide anyone the ability to generate and organize markdown notes directly from the command line in a matter of seconds.  Don't get delayed and frustrated with slow IDE editors and their cumbersome GUI interfaces. Fully customizable templates allow you to take full control of your notes!

![Scribe](https://media4.giphy.com/media/C66KH6ed9B0gc4Likj/giphy.gif?cid=790b761120cb0f1891af4431ef679cd2a26b0cc909742f96&rid=giphy.gif&ct=g)
<br>
1. [Overview](#overview)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)

# Overview

[Back to Top](#note-taker)

* Compatible with Windows, Linux and MacOS
* This Python3 utility simply creates [markdown](https://en.wikipedia.org/wiki/Markdown) files one the fly... it is NOT a markdown editor.  THe [Requirements](#requirements) section has some third party WYSIWYG recommendations.  If you have any suggestions feel free to email me and it will get added to the list.
* Following the '*Less Is More*' way of thinking, Scribe limits folder nesting to two levels.  This can be changed through the config file by updating the 'classifications' setting.
* The first time Scribe runs, it will prompt you for where you wish to create your notes.  Make sure this folder alreday exists beforehand.

# Requirements

[Back to Top](#note-taker)

This utility is a Python3 script.  Make sure the following requirements have bene installed"

* [Python3](https://www.python.org/downloads/)
* [PyYAML](https://pyyaml.org/)
* [Python-dotenv](https://pypi.org/project/python-dotenv/)

A WYSIWYG markdown editor is highly recommended.  Below are two worth considering:

* [Typora](https://typora.io/)
* [UNotes](https://marketplace.visualstudio.com/items?itemName=ryanmcalister.Unotes)

# Installation

[Back to Top](#note-taker)

This is a command line interface.  To install, become familiar with your operating system's [terminal](https://itconnect.uw.edu/learn/workshops/online-tutorials/web-publishing/what-is-a-terminal/) app.
Run terminal, navigate to the install directory of your choice (ex. '<span class="colour" style="color:rgb(206, 145, 120)">/Users/jsmith/Documents/Projects</span>') and run the following GIT command:
`git clone https://github.com/tedweb/scribe.git`

![image](https://raw.githubusercontent.com/tedweb/scribe/main/resources/git_clone.png)

Once the code has been downloaded, run the following command to execute:
`python3 scribe.py`

Alternatively, a safer method would include the path.  Using the path example from above:
`python3 ~/Documents/Projects/Scribe/scribe.py`

The first run will prompt you to enter the path to your notes folder (ex. '<span class="colour" style="color:rgb(206, 145, 120)">/Users/jsmith/Documents/Notes</span>'). If this folder does not exist, create it.  Once created, you are ready to start creating some markdown notes!
![image](https://raw.githubusercontent.com/tedweb/scribe/main/resources/Screenshot.png)

<br>
<br>
<br>
# Configuration

[Back to Top](#note-taker)

The `config.yml` file is a YAML file allowing for customizations of the app includeing:

* ignore: Folders to ignore and prevent from displaying.
* working directory: There your note files are kept.
* template: Custom templates can be created and assigned to specific directories within your notes folder.

# Usage

[Back to Top](#note-taker)
<br>
* Text