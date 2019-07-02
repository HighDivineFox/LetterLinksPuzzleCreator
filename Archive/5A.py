import mmap
import re
import json
from RemoveWords import fixup
from GlobalSettings import category, FiveLetterWords, maxWords, file_path

orders = [
            [0, 1, 2, 3, 4],
            [0, 1, 3, 2],
            [0, 1, 3, 4],
            [1, 2, 3, 4],
            [1, 3, 2],
            [1, 3, 4],
            [2, 1, 0],
            [2, 1, 3, 4],
            [2, 3, 1, 0],
            [2, 3, 4],
            [3, 1, 0],
            [3, 1, 2],
            [3, 2, 1, 0],
            [4, 3, 1, 0],
            [4, 3, 1, 2],
            [4, 3, 2, 1, 0]
        ]

letterConfig = "5A"
#category = "Deep Sea"
allwords = FiveLetterWords

# This does't exist anymore
#file_path = "D:\\Unity Projects\\HexWords\\Assets\\Resources\\Levels\\LevelPack1.json"

file = open('Words.txt')
lines = file.readlines()
s = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)

fileSet = list(set(lines))
fileSet = set(line.rstrip() for line in fileSet)

def checkWord(wordToCheck):
    global file
    global lines
    global fileSet

    if wordToCheck in fileSet:
        return True

    return False

def MainWork(_word):
    global file
    global lines
    global fileSet
    global letterConfig
    global category

    file = open('Words.txt')
    lines = file.readlines()

    fileSet = list(set(lines))
    fileSet = set(line.rstrip() for line in fileSet)

    word = _word.lower()
    letters = [word[0], word[1], word[2], word[3], word[4]]

    foundWords = []

    for i in range(len(orders)):
        a = ""
        for j in range(len(orders[i])):
                a += letters[orders[i][j]]
                if(len(a) >= 2):
                    if checkWord(a):
                        foundWords.append(a)

    foundWords.sort()
    foundWords.sort(key = lambda s: len(s))
    foundWords.reverse()

    foundWords = list(dict.fromkeys(foundWords)) # Remove duplicates

    while(len(foundWords) > maxWords):
        foundWords.pop()

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
        'letterConfig' : letterConfig,
        'mainWord' : word,
        'answers' : foundWords
    })

    with open(file_path, 'w') as json_file:
        json.dump(data_to_save, json_file, indent=4)

print(len(allwords))
for x in range(len(allwords)):
    print("Seaching:" + allwords[x])
    MainWork(allwords[x])

