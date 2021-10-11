import csv
import json
import numpy as np

def array2Json(array):
    parrain = {
        "name" : array[-1],
        "filleuls_potentiels":array[:5]
    }
    return parrain

def getMultipleChoice(a,b):
    return [i for i, j in zip(a, b) if i == j]

def returnMatches(a, b):
    tab_mutiple_index = [9, 11, 18, 19, 21, 23, 24, 26, 31, 32]
    multiple_choice = []
    for i, matches in enumerate(tab_mutiple_index):
        if(len(a[matches].split(","))>1 or len(b[matches].split(","))>1):
            multiple_choice.append(getMultipleChoice(a[matches].split(","),b[matches].split(",")))
    return np.hstack([i for i, j in zip(a, b) if i == j] + multiple_choice)

with open('parrain.csv', newline='') as p:
    reader = csv.reader(p)
    parrain_data = list(reader)
with open('filleul.csv', newline='') as f:
    reader_f = csv.reader(f)
    filleul_data = list(reader_f)

all_top_5_match = []
for filleul in filleul_data:
    top_5_match = []
    for parrain in parrain_data:
        count_match = len(returnMatches(filleul, parrain))
        top_5_match.append((parrain[2]+' '+parrain[3], count_match))
    top_5_match.pop(0)
    top_5_match = sorted(top_5_match, key=lambda x: int(x[1]), reverse=True)
    top_5_match = top_5_match[:5]
    top_5_match.append(filleul[2] + " " + filleul[3])
    all_top_5_match.append(top_5_match)
all_top_5_match.pop(0)
with open('data2.json', 'w') as outfile:
    for match in all_top_5_match:
        json.dump(array2Json(match), outfile, indent=4, ensure_ascii=False)
