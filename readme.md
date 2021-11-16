# Graduation Photo Renamer

## How to use

This application will rename all photos of current year students from past years and store them in a new folder structure based on class. The idea is to be able to easily drag and drop the kids into something like Movie Maker or iMovie and have each students grade P-6 photos show one after the other in last name role order.

You will need to have a **copy** of the last 7 years worth of student photos. You will need to remove any non applicable classes and prepare the folder structure as below.

The database is built based on their grade 6 photo names. If the grade 6 photo names are in format *"firstname_lastname.jpg"* you will need to pass in a command line switch that will ensure the photos are renamed to lastname_firstname. 
The command line switch is **--first-last**

If the grade 6 photo names are already last_first, run app without any switches.

Any photos that are unable to match will be put inside a folder called "failures-move-manually"

### Folder structure IMPORTANT

*App should be run from the root project folder*

Note that each year folder must be name as the year only. ie "2020" **not "Students 2020"**

Note that each folder year should only contain the classes of which the current students would have been in.

Note that in the below example, the database will be built off the current year (2022) which contains grade 6 photos stored in their respective class folders. In this example, we have the undesirable naming convention of *first_last.jpg* ie. *harry_potter.jpg*. This means we must pass the *--last-first* parameter when we run the app.

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