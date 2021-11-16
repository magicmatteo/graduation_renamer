# Graduation Photo Renamer

## How to use

This application will rename all photos of current year students from past years and store them in a new folder structure based on class. The idea is to be able to easily drag and drop the kids into something like Movie Maker or iMovie and have each students grade P-6 photos show one after the other in last name role order.

You will need to have a **copy** of the last 7 years worth of student photos. You will need to remove any non applicable classes and prepare the folder structure as below.

The database is built based on their grade 6 photo names. If the grade 6 photo names are in format *"firstname_lastname.jpg"* you will need to answer *'n'* in the menu prompt.

Any photos that are unable to match will be put inside a folder called "failures-move-manually"

### Folder structure IMPORTANT

*App should be run from the root project folder*

Note that each year folder must be name as the year only. ie "2020" **not "Students 2020"**

Note that each folder year should only contain the classes of which the current students would have been in.

Note that in the below example, the database will be built off the current year (2022) which contains grade 6 photos stored in their respective class folders. In this example, we have the undesirable naming convention of *first_last.jpg* ie. *harry_potter.jpg*. This means we must answer 'n' in the menu prompt.

```
project
│   README.md
│   main.py
│   app.exe
│   
│
└───2020
│   │   
│   └───4S
│   │   │   doe_jane.jpg
│   │   │   smith_john.jpg
│   │   │   ...
│   │
│   └───4G
│   │   │
│   │   │   weasley_ron.jpg
│   │   │   potter_harry.jpg
│   │   │   ...
│   │...
│   
└───2021
│   │   
│   └───5W
│   │   │   jane_doe.jpg
│   │   │   john_smith.jpg
│   │   │   ...
│   │
│   └───5K
│   │   │
│   │   │   ron_weasley.jpg
│   │   │   harry_potter.jpg
│   │   │   ...
│   │...
│   
└───2022
│   │   
│   └───6H
│   │   │   jane_doe.jpg
│   │   │   john_smith.jpg
│   │   │   ...
│   │
│   └───6R
│   │   │
│   │   │   ron_weasley.jpg
│   │   │   harry_potter.jpg
│   │   │   ...
│   │...
```

## Example runthrough

### Using Python
1. Download and install Python 3 from [here](https://www.python.org/downloads/)
2. Prepare folder structure
3. Shift + Right-Click in project root folder in File Explorer -> Click *Open in Powershell*
4. From powershell run:
        python ./main.py

### Using compiled windows EXE
1. Prepare folder structure
2. Run main.exe from project root folder and follow prompt

## Compiling .exe for Windows

Assuming python 3 installed on Windows.

1. Install pyinstaller
        pip install -r ./requirements.txt
2. Run pyinstaller on main.py
        pyinstaller ./main.py

Application will be built into ./dist/main


