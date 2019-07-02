import mmap
import re
import json
from RemoveWords import fixup
from GlobalSettings import category, maxWords, file_path
from orders import _7A as letterMix

file = open('Words.txt')
lines = file.readlines()
s = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)

fileSet = list(set(lines))
fileSet = set(line.rstrip() for line in fileSet)

def checkWord(wordToCheck):
    global fileSet

    if wordToCheck in fileSet:
        return True

    return False

def MainWork(_word):
    global file
    global lines
    global fileSet
    global category

    file = open('Words.txt')
    lines = file.readlines()

    fileSet = list(set(lines))
    fileSet = set(line.rstrip() for line in fileSet)

    word = _word.lower()
    letters = []

    for x in word:
        letters.append(x)

    foundWords = []

    for i in range(len(letterMix['orders'])):
        a = ""
        for j in range(len(letterMix['orders'][i])):
                a += letters[letterMix['orders'][i][j]]
                if(len(a) >= 2):
                    if checkWord(a):
                        foundWords.append(a)

    foundWords.sort()
    foundWords.sort(key = lambda s: len(s))
    foundWords.reverse()

    foundWords = list(dict.fromkeys(foundWords)) # Remove duplicates

    print(foundWords)

    wordsToRemove = input('Remove words? (seperate with ",") ')

    splitWords = wordsToRemove.split(",")
    print(splitWords)

    if len(splitWords) > 0:
        saveResults = input('Save results? ')

    if saveResults == 'n' or saveResults == 'N':
        fixup(splitWords)
        file.close()
        restart = input('Run word search again? ')
        if restart == 'n' or restart == 'N':
            return
        MainWork(word)
        return

    data_to_save = {}
    data_to_save['Items'] = []

    mostRecentLevel = -1
    mostRecentCategory = ""

    with open(file_path) as json_file2:
        loadedData = json.load(json_file2)

        for p in loadedData['Items']:
            mostRecentLevel = p['id']
            mostRecentCategory = p['category']

            data_to_save['Items'].append({ # Append the existing data_to_save in the file
                'category' : p['category'],
                'id' : p['id'],
                'unlocked' : p['unlocked'],
                'letterConfig' : p['letterConfig'],
                'mainWord' : p['mainWord'],
                'answers' : p['answers']
            })

    data_to_save['Items'].append({
        'category' : category,
        'id' : mostRecentLevel+1,
        'unlocked' : True if mostRecentCategory != category else False,
        'letterConfig' : letterMix['letterConfig'],
        'mainWord' : word,
        'answers' : foundWords
    })

    if len(data_to_save['Items'][len(data_to_save['Items'])-1]['answers']) > 14:
        print("Warning: more than 14 answers. Won't fit on the game screen")
        print(len(data_to_save['Items'][len(data_to_save['Items'])-1]['answers']))

    with open(file_path, 'w') as json_file:
        json.dump(data_to_save, json_file, indent=4)

for x in range(len(letterMix['words'])):
    print("\nSeaching:" + letterMix['words'][x])
    MainWork(letterMix['words'][x])

