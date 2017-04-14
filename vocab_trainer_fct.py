"""Vocab-Trainer functions

    This file provides functions for the vocab-trainer 
    application.

    @author Florian Dahlitz
"""
import random
import os


def get_path_mode(settingsFile):
    """Get path mode

        Returns the path of the file containing the vocab-pairs and 
        the mode of the run.
    """
    fullPath = os.path.dirname(os.path.realpath(__file__))
    settings = {}
    with open(fullPath + settingsFile, "r") as settFile:
        for number, line in enumerate(settFile):
            line = line.strip()
            parts = line.split(" ")
            if number == 0:
                settings[parts[0]] = parts[1]
            else:
                settings[parts[0]] = parts[1]

    return [fullPath + settings["path"], settings["mode"]]


def get_vocab(filePath, mode, reverse = False):
    """Get vocab

        Returns the vocab-pairs.
    """
    # must be a dict including key=tuple, value=tuple
    words = {}

    # reads in with forms
    if mode == 2:
        with open(filePath, "r") as file:
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

    # reads in without forms
    else:
        with open(filePath, "r") as file:
            for line in file:
                line = line.strip()
                parts = line.split(" - ")
                lang1 = tuple(parts[0].split(", "))
                lang2 = tuple(parts[1].split(", "))
                if reverse == False:
                    words[lang1] = lang2
                else:
                    words[lang2] = lang1
    
    return words


def get_random(words, wordsReverse = False):
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

