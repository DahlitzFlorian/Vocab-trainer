"""Vocab-Trainer

    This application is a lightweighted easy to handle
    vocab-trainer written in Python 3.4

    @author Florian Dahlitz
"""
import vocab_trainer_fct as functions
import os
import re


# getting the path to the file storing the vocab to train on
path_mode = functions.get_path_mode("vocab_settings.txt")
path = path_mode[0]
mode = path_mode[1]

# receiving mode-info and vocab-pairs
vocab = functions.get_vocab(path, mode)

# setting up the field to play on
userInput = None
field = {i : None for i in range(1, 26)}
controls = (3, 8, 13, 18, 25)

# creating vocab-lists
numberEntireVocab = len(vocab)
vocabLeft = numberEntireVocab
vocabFinished = 0

# adding forms input if the mode was selected
if mode == 2:
    userFormsInput = None

# creats the window
os.system("cls" if os.name == "nt" else "clear")
print("{} finished. {} left. Entire: {}".format(vocabFinished, vocabLeft, numberEntireVocab))
print("-"*50)

# training on vocab
while vocabLeft != 0:
    referencedField = 25
    while(referencedField > 0):
        # check if vocab is on the referenced field
        if field[referencedField] != None:
            os.system("cls" if os.name == "nt" else "clear")
            print("{} finished. {} left. Entire: {}".format(vocabFinished, vocabLeft, numberEntireVocab))
            print("-"*50)

            # checks if the referenced field is a controlling field
            if referencedField in controls:
                currVocab = field[referencedField] # currVocab is tuple

                # takes the vocab on the referenced field
                vocabKey = currVocab[0]
                keys = ', '.join(map(str, vocabKey))
                print(keys)

                if mode == 2:
                    formsTupUser = currVocab[1][0]
                    valueTup = currVocab[1][1]
                else:
                    valueTup = currVocab[1]

                ##############################################
                # should remove everything in brackets such as (to)
                valueList = []
                for value in valueTup:
                    valueList.append(value)

                valueTupUser = []   # first it will be a list to be mutable
                for value in valueList:
                    value = re.sub(r'\(.*?\)\ *', '', value)
                    valueTupUser.append(value)

                valueTupUser = tuple(valueTupUser)
                # end of it
                #############################################

                # asks for forms input if mode was selected
                if mode == 2:
                    userFormsInput = input("Forms: ")
                    userFormsInput = userFormsInput.split(", ")
                    userFormsList = []
                    for form in userFormsInput:
                        userFormsList.append(form)

                    userFormsInput = tuple(userFormsList)
                    userInput = input("Translation: ")
                    if (userInput in valueTupUser) and (formsTupUser == userFormsInput):
                        if referencedField == 25:
                            field[referencedField] = None
                            vocabLeft -= 1
                            vocabFinished += 1
                        else:
                            all_forms = formsTupUser
                            values = valueTupUser
                            print("-"*50)
                            print("{} - {} - {}".format(keys, ", ".join(all_forms), ", ".join(values)))
                            print("-" * 50)
                            input("Press Enter to continue.")

                            field[referencedField + 1] = currVocab
                            field[referencedField] = None
                    else:
                        all_forms = formsTupUser
                        values = valueTupUser
                        print("-" * 50)
                        print("{} - {} - {}".format(keys, ", ".join(all_forms), ", ".join(values)))
                        print("-" * 50)
                        input("Press Enter to continue.")
                        vocab[vocabKey] = (formsTupUser, valueTup)
                        field[referencedField] = None
                # does not asks for forms if mode was not selected
                else:
                    userInput = input("Translation: ")
                    if userInput in valueTupUser:
                        if referencedField == 25:
                            field[referencedField] = None
                            vocabLeft -= 1
                            vocabFinished += 1
                        else:
                            print("-" * 50)
                            print("{} - {}".format(keys, ", ".join(valueTupUser)))
                            print("-" * 50)
                            input("Press Enter to continue.")

                            field[referencedField + 1] = currVocab
                            field[referencedField] = None
                    else:
                        values = valueTupUser
                        print("-" * 50)
                        print("{} - {}".format(keys, ", ".join(values)))
                        print("-" * 50)
                        input("Press Enter to continue.")
                        vocab[vocabKey] = valueTup
                        field[referencedField] = None
            # starting point -> displays the vocab-pair
            elif referencedField == 1:
                field[referencedField+1] = field[referencedField]
                # get new pair
                if bool(vocab) == True:
                    randomKey = functions.get_random(vocab)
                    for tup in vocab:
                        if randomKey in tup:
                            randomKey = tup
                    field[referencedField] = (randomKey, (vocab[randomKey]))
                    if mode == 2:
                        forms = vocab[randomKey][0]
                        values = vocab[randomKey][1]
                        print("{} - {} - {}".format(", ".join(randomKey), ", ".join(forms), ", ".join(values)))
                    else:
                        print("{} - {}".format(", ".join(randomKey), ", ".join(vocab[randomKey])))

                    input("Press Enter.")
                    del vocab[randomKey]
                # None if vocab is empty
                else:
                    field[referencedField] = None
            else:
                field[referencedField+1] = field[referencedField]
                field[referencedField] = None
            referencedField -= 1
        # get new vocab pair
        elif referencedField == 1:
            # new pair
            if bool(vocab) == True:
                randomKey = functions.get_random(vocab)
                for tup in vocab:
                    if randomKey in tup:
                        randomKey = tup
                field[referencedField] = (randomKey, (vocab[randomKey]))
                if mode == 2:
                    print("{} - {} - {}".format(", ".join(randomKey), ", ".join(vocab[randomKey][0]), ", ".join(vocab[randomKey][1])))
                else:
                    print("{} - {}".format(", ".join(randomKey), ", ".join(vocab[randomKey])))

                input("Press Enter.")

                del vocab[randomKey]
            # None if vocab is empty
            else:
                field[referencedField] = None
            referencedField -= 1
        else:
            referencedField -= 1
    # closes application
    if userInput == "0":
        vocabLeft = 0
