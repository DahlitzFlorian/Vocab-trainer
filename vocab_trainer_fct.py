"""Vocab-Trainer functions

    This file provides functions for the vocab-trainer 
    application.

    @author Florian Dahlitz
"""
import random
import os


def getPath(settingsFile) :
    """Get path

        Returns the path of the file containing the vocab-pairs.
    """
    fullPath = os.path.dirname(os.path.realpath(__file__))
    settings = {}
    settFile = open(fullPath + settingsFile, "r")
    for line in settFile :
        line = line.strip()
        parts = line.split(" ")
        settings[parts[0]] = parts[1]
    settFile.close()

    return fullPath + settings["path"]


def getFromFile(filePath, reverse = False) :
    """Get from file

        Returns the vocab-pairs and the mode.
    """
    # must be a dict including key=tuple, value=tuple
    words = {}
    is_latin = False

    # reads in with forms
    if "latin" in filePath:
        is_latin = True
        file = open(filePath, "r")
        for line in file:
            line = line.strip()
            parts = line.split(" - ")
            lang1 = tuple(parts[0].split(", "))
            forms = tuple(parts[1].split(", "))
            lang2 = tuple(parts[2].split(", "))
            if reverse == False:
                words[lang1] = (forms,lang2)
            else:
                words[lang2] = lang1
    
        file.close()
    # reads in without forms
    else:
        file = open(filePath, "r")
        for line in file:
            line = line.strip()
            parts = line.split(" - ")
            lang1 = tuple(parts[0].split(", "))
            lang2 = tuple(parts[1].split(", "))
            if reverse == False:
                words[lang1] = lang2
            else:
                words[lang2] = lang1

        file.close()
    
    return (words, is_latin)


def getRandom(words, wordsReverse = False) :
    """Get random

        Returns a random key of the given vocab-list.
    """
    # choosing without reverse vocab
    if wordsReverse == False:
        return random.choice(list(random.choice(list(words.keys()))))
    # choosing with reverse vocab
    else:
        choice = random.randint(0,1)
        if choice == 0:
            return random.choice(list(random.choice(list(words.keys()))))
        else:
            return random.choice(list(random.choice(list(wordsReverse.keys()))))

