import json

file_path = ".\\levels.json"

data_to_save = {}
data_to_save['Items'] = []

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

for item in data_to_save['Items']:
    if len(item['answers']) > 14:
        print(item['mainWord'])

#print(len(data_to_save['Items']))