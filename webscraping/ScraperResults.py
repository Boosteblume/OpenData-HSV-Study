import os
import json

file_list = []
for i in os.listdir(r"webscraping"):
    if i.endswith(".json"):
        i = "webscraping/" + i
        file_list.append(i)

def merge_JsonFiles(filename):
    result = list()
    for f1 in filename:
        with open(f1, 'r') as infile:
            result.extend(json.load(infile))

    with open('test.json', 'w') as output_file:
        json.dump(result, output_file)

merge_JsonFiles(file_list)


with open('test.json') as file:
   data = json.load(file)

print("Anzahl an Einträgen: ", len(data))

subs = ['dfb', 'sonne', 'Derby']

positive = ["gewinn", 
            "rückkehr", 
            "rückkehrer", 
            "teilnahme", 
            "aufbautraining", 
            "teamtraining", 
            "neuzugang", 
            "verpflichtung",
            "transfer", 
            "gerücht", 
            "fit",
            "einsatzbereit"]

negative = ["ausfall",
            "op",
            "verletzung",
            "pause",
            "separates training",
            "individuelles training",
            "krankheit",
            "trainingsausfall", 
            "fehlt",
            "transfermarkt",
            "ersatz",
            "umsehen",
            "wechsel",
            "gerücht",
            "abgang",
            "ablösessumme",
            "hiobsbotschaft"]

#transform all charcters to lowercase
data = [x.lower() for x in data]
positive = [x.lower() for x in positive]
negative = [x.lower() for x in negative]

resultp = []
for i in positive:
    for j in data:
        if i in j:
            resultp.append(i)

print("This is the positive result: " , len(resultp))

resultn = []
for i in negative:
    for j in data:
        if i in j:
            resultn.append(i)

print("This is the negative result: " , len(resultn))