# ITP 115, Spring 2023
# Final Project
# Name: Kristen Won
# Email: kjwon@usc.edu
# Section: 31850
# Filename: main_won_kristen.py
# Description:
# This program allows the user to take actions
# to learn about roller coasters from a database.

import helper
import user_io

# dictionary of command options for the user
def makeOptionsDict():
    myDict = {
        "A":"Amusement parks",
        "B":"Number of coasters",
        "C":"Number of wooden coasters",
        "D":"Loopiest coaster",
        "E":"Tallest coaster",
        "F":"Find coasters",
        "Q":"Quit"
    }

    return myDict

def main():
    print("Roller Coasters from around the world")
    # list of roller coasters
    list = helper.makeCoastersList("roller_coasters.csv")
    # dictionary of options
    dict = makeOptionsDict()
    # displays the command options
    user_io.displayDict(dict)
    userChoice = user_io.getUserOption(dict)
    while userChoice != "Q":
        if userChoice == "A": # names of amusement parks
            user_io.makeParksFile(list)
            user_io.displayDict(dict)
            userChoice = user_io.getUserOption(dict)
        if userChoice == "B": # displays number of coasters
            user_io.displayNumCoasters(list)
            user_io.displayDict(dict)
            userChoice = user_io.getUserOption(dict)
        if userChoice == "C": # displays number of wooden coasters
            user_io.displayNumWoodenCoasters(list)
            user_io.displayDict(dict)
            userChoice = user_io.getUserOption(dict)
        if userChoice == "D": # displays info about the loopiest coaster
            user_io.displayLoopiestCoaster(list)
            user_io.displayDict(dict)
            userChoice = user_io.getUserOption(dict)
        if userChoice == "E": # displays info about the tallest coaster
            user_io.displayTallestCoaster(list)
            user_io.displayDict(dict)
            userChoice = user_io.getUserOption(dict)
        if userChoice == "F": # finds coaster based on search phrase
            user_io.findCoasters(list)
            user_io.displayDict(dict)
            userChoice = user_io.getUserOption(dict)

main()