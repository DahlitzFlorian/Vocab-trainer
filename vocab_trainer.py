import vocab_trainer_fct as voc
import os
import re


path = voc.getPath("vocab_settings.txt")
vocab_info = voc.getFromFile(path)
vocab = vocab_info[0]
userInput = None
field = {i : None for i in range(1, 26)}    # create field with default: no vocab
controls = (3, 8, 13, 18, 25)   # places, where user is asked for translation
numberEntireVocab = len(vocab)
vocabLeft = numberEntireVocab
vocabFinished = 0

if vocab_info[1] == True:
    userFormsInput = None


os.system("cls")
print("{} finished. {} left. Entire: {}".format(vocabFinished, vocabLeft, numberEntireVocab))
print("-"*50)

while vocabLeft != 0:

    referencedField = 25

    while(referencedField > 0):

        if field[referencedField] != None:

            os.system("cls")
            print("{} finished. {} left. Entire: {}".format(vocabFinished, vocabLeft, numberEntireVocab))
            print("-"*50)

            if referencedField in controls:
                currVocab = field[referencedField] # currVocab is tuple
                
                vocabKey = currVocab[0]
                keys = ', '.join(map(str, vocabKey))
                print(keys)

                if vocab_info[1] == True:
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

                if vocab_info[1] == True:
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
                            os.system("pause")

                            field[referencedField + 1] = currVocab
                            field[referencedField] = None

                    else:
                        all_forms = formsTupUser
                        values = valueTupUser
                        print("-" * 50)
                        print("{} - {} - {}".format(keys, ", ".join(all_forms), ", ".join(values)))
                        print("-" * 50)
                        os.system("pause")
                        vocab[vocabKey] = (formsTupUser, valueTup)
                        field[referencedField] = None
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
                            os.system("pause")

                            field[referencedField + 1] = currVocab
                            field[referencedField] = None

                    else:
                        all_forms = formsTupUser
                        values = valueTupUser
                        print("-" * 50)
                        print("{} - {} - {}".format(keys, ", ".join(all_forms), ", ".join(values)))
                        print("-" * 50)
                        os.system("pause")
                        vocab[vocabKey] = valueTup
                        field[referencedField] = None

            elif referencedField == 1:
                field[referencedField+1] = field[referencedField]
                if bool(vocab) == True:
                    randomKey = voc.getRandom(vocab)
                    for tup in vocab:
                        if randomKey in tup:
                            randomKey = tup
                    field[referencedField] = (randomKey, (vocab[randomKey]))
                    if vocab_info[1] == True:
                        forms = vocab[randomKey][0]
                        values = vocab[randomKey][1]
                        print("{} - {} - {}".format(", ".join(randomKey), ", ".join(forms), ", ".join(values)))
                    else:
                        print("{} - {}".format(", ".join(randomKey), ", ".join(vocab[randomKey])))

                    input("Press Enter.")

                    del vocab[randomKey]
                else:
                    field[referencedField] = None

            else:
                field[referencedField+1] = field[referencedField]
                field[referencedField] = None
        
            referencedField -= 1

        elif referencedField == 1:
            if bool(vocab) == True:
                randomKey = voc.getRandom(vocab)
                for tup in vocab:
                    if randomKey in tup:
                        randomKey = tup
                field[referencedField] = (randomKey, (vocab[randomKey]))
                if vocab_info[1] == True:
                    print("{} - {} - {}".format(", ".join(randomKey), ", ".join(vocab[randomKey][0]), ", ".join(vocab[randomKey][1])))
                else:
                    print("{} - {}".format(", ".join(randomKey), ", ".join(vocab[randomKey])))

                input("Press Enter.")

                del vocab[randomKey]
            else:
                field[referencedField] = None

            referencedField -= 1

        else:
            referencedField -= 1

    if (userInput == "0") or (userFormsInput == "0"):

        vocabLeft = 0
