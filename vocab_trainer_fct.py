import random


def getPath(settingsFile) :

    fullPath = "C:/Users/Example/" # add full path to dir with files here
    settings = {}
    settFile = open(fullPath + settingsFile, "r")

    for line in settFile :

        line = line.strip()
        parts = line.split(" ")
        settings[parts[0]] = parts[1]
    
    settFile.close()

    return fullPath + settings["path"]

def getFromFile(filePath, reverse = False) :

    words = {}  # must be a dict including key=tuple, value=tuple
    is_latin = False

    if "latin" in filePath:
        is_latin = True

        file = open(filePath, "r")

        for line in file :

            line = line.strip()
            parts = line.split(" - ")
            lang1 = tuple(parts[0].split(", "))
            forms = tuple(parts[1].split(", "))
            lang2 = tuple(parts[2].split(", "))

            if reverse == False :
                words[lang1] = (forms,lang2)
            else :
                words[lang2] = lang1
    
        file.close()
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

    if wordsReverse == False :
        return random.choice(list(random.choice(list(words.keys()))))
    else :
        choice = random.randint(0,1)

        if choice == 0 :
            return random.choice(list(random.choice(list(words.keys()))))
        else :
            return random.choice(list(random.choice(list(wordsReverse.keys()))))

