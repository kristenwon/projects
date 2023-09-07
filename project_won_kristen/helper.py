# ITP 115, Spring 2023
# Final Project
# Name: Kristen Won
# Email: kjwon@usc.edu
# Section: 31850
# Filename: helper.py
# Description:
# This program allows the user to take actions
# to learn about roller coasters from a database.
# This file contains functions that the main and user
# interface files will use.

def makeCoastersList(filenameStr):
    # list of dictionaries (coasters)
    # each coasters' keys are strings from header row
    # values are strings containing information from one row
    coasters = []
    fileIn = open(filenameStr, "r")
    headerLine = fileIn.readline().strip()
    headerLine = headerLine.split(",")
    for line in fileIn:
        int = 0
        mydict = {}
        line = line.split(",")
        for i in headerLine:
            mydict[i] = line[int]
            int += 1
        coasters.append(mydict)
    fileIn.close()
    return coasters

def getUniqueParkNames(coastersList):
    parkNames = []
    # for each coaster
    for i in coastersList:
        name = i["park"]
        # if name is unique add it to the list
        if name not in parkNames:
            parkNames.append(name)

    parkNames.sort()
    return parkNames

def getLoopiestCoaster(coastersList):
    # tracks the biggest loop count
    maxLoops = 0
    loopiestCoaster = {}

    for coaster in coastersList:
        # determines num of inversions for each coaster
        # based on dictionary value
        numInversions = coaster.get("num_inversions")
        if numInversions.isdigit():
            loops = int(numInversions)
            if loops > maxLoops:
                maxLoops = loops
                loopiestCoaster = coaster

    return loopiestCoaster

def getTallestCoaster(coastersList):
    # tracks the tallest height
    maxHeight = 0
    tallestCoaster = {}

    for coaster in coastersList:
        # determines height for each coaster
        # based on dictionary value
        numHeight = coaster.get("height")
        if numHeight.isdigit():
            height = int(numHeight)
            if height > maxHeight:
                maxHeight = height
                tallestCoaster = coaster

    return tallestCoaster