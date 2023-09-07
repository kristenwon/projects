# ITP 115, Spring 2023
# Final Project
# Name: Kristen Won
# Email: kjwon@usc.edu
# Section: 31850
# Filename: user_io.py
# Description:
# This program allows the user to take actions
# to learn about roller coasters from a database.
# This file defines all the commands a user
# can decide to do to learn about roller coasters.

import helper

# displays the options for user commands
def displayDict(optionsDict):
    keyslist = list(optionsDict.keys())
    keyslist.sort()
    for i in keyslist:
        print(i, "->", optionsDict[i])

# gets the user's command choice
def getUserOption(optionsDict):
    userOption = input("Option: ")
    userOption = userOption.strip().upper()
    while userOption not in optionsDict.keys():
        userOption = input("Option: ")
        userOption = userOption.strip().upper()

    return userOption

# prints the total number of roller coasters in the database
def displayNumCoasters(coastersList):
    print("The total number of coasters is", len(coastersList), "\n")

# prints the total number of wooden roller coasters in the database
def displayNumWoodenCoasters(coastersList):
    woodenCoasters = 0
    for i in coastersList:
        if i["material_type"] == "Wooden":
            woodenCoasters += 1

    print("The total number of wooden coasters is", woodenCoasters, "\n")

# prints information about the coaster if there is valid information
def displayCoaster(coasterDict):
    print(coasterDict["name"], "[" + coasterDict["park"] + "]")
    if coasterDict["speed"] != "":
        print("\tSpeed =", coasterDict["speed"], "mph")
    if coasterDict["height"] != "":
        print("\tHeight =", coasterDict["height"], "ft")
    if coasterDict["length"] != "":
        print("\tLength =", coasterDict["length"], "ft")
    if coasterDict["num_inversions"] != "" and int(coasterDict["num_inversions"]) > 0:
        print("\tLoops =", coasterDict["num_inversions"])
    print("\tStatus is", coasterDict["status"])

# prints information about the roller coaster with the most loops
def displayLoopiestCoaster(coastersList):
    loopiest = helper.getLoopiestCoaster(coastersList)
    displayCoaster(loopiest)

# prints information about the tallest rollercoaster
def displayTallestCoaster(coastersList):
    tallest = helper.getTallestCoaster(coastersList)
    displayCoaster(tallest)

# creates a file with names of amusement parks
def makeParksFile(coastersList):
    names = helper.getUniqueParkNames(coastersList)
    fileOut = open("amusement_parks.txt", "w")
    # write into the file the names of amusement parks
    print("Amusement parks in alphabetical order:", file=fileOut)
    count = 0
    for i in names:
        print(i, file=fileOut)
        count += 1
    fileOut.close()
    print("There are", count, "unique parks.")
    print("The park names were saved to amusement_parks.txt\n")

# searches thru the database for a coaster with the user
# specified keyword
def findCoasters(coastersList):
    userPhrase = input("Enter a search phrase: ").strip().lower()
    coaster = 0
    for i in coastersList:
        # if the phrase is contained in the coaster name or park name
        if userPhrase in i["name"].lower() or userPhrase in i["park"].lower():
            displayCoaster(i)
            coaster += 1
    if coaster != 0:
        print("Found", coaster, "coasters that contain '" + userPhrase + "'\n")
    else:
        print("No coasters contain '" + userPhrase + "'\n")