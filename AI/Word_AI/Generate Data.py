import json
import random
import sys
from collections import defaultdict


def wort_erkennen(zeichenfolge):
    words = dataprefixes
    possibilities = {}
    possibilities = defaultdict(list)
    global highest_poss

    zeichenfolge = zeichenfolge.lower()

    words[format-2] = [word for word in words[format-2] if len(word)-len(zeichenfolge) <= 2 and len(word)-len(zeichenfolge) >= -2]

    for i in range(0,len(words[format-2])):
        matches = 0

        for number, char in enumerate(words[format-2][i].lower()):
            if char in zeichenfolge[number - 2 if number >= 2 else number - 1 if number >= 1 else number:number + 2 if number < len(zeichenfolge) - 2 else number + 1 if number < len(zeichenfolge) - 1 else number if number < len(zeichenfolge) else len(zeichenfolge) - 1]:
                matches += 1


        if matches / max(len(words[format-2][i]), len(zeichenfolge)) > 0.8:
            possibilities[words[format-2][i]].append(matches / max(len(words[format-2][i]), len(zeichenfolge)))

    if len(possibilities) > 0:
        highest_poss = max(possibilities,key=possibilities.get)
        return highest_poss
        
    return ""

dataprefixes = []
dots = 0

with open(f"AIDATA/datawords.json", "r", encoding="utf-8") as ai:
    data = json.load(ai)

for i in range(0,len(data)):
    dataprefixes.append([])
    for keys in data[i]:
        dataprefixes[i].append(keys)

#sentence = int(input("How many sentences?\n"))
start = input("Enter a start of a sentence. (2 - 10 words)\n")
try:
    limit = int(input("Enter an upper limit to Format. Press enter to skip.\n"))
except:
    limit = len(data) + 1
print(limit)

format = len(start.split(" "))
sentence = 10


while dots < sentence:

    if start in data[format-2]:
        new_word = data[format-2][start][random.randint(0,len(data[format-2][start])-1)]
        
        if format < limit and start + " " + new_word in data[format-1]:
            format += 1
            start = start + " " + new_word
            print(f"\n\033[38;2;57;255;20mSwitched to Format {format}.\033[0m")
        else:
            i = 0
            while start[i] != " ":
                i += 1
            start = start[i + 1:]+ " " + new_word
        sys.stdout.write(new_word + " ")

    else:
        if wort_erkennen(start) != "":
            print("\033[33mSpelling not correct. Going along with the best match.\33[0m")
            start = highest_poss
            sys.stdout.write(highest_poss + " ")

        else:
            if format > 2:
                format = len(start.split(" ")) - 1
                while " " in start and not start.endswith(" "):
                    start = start[:-1]
                start = start[:-1] if start.endswith(" ") else start
                print(f"\033[31mWord not found. Switched to Format {format}. Deacreased words to {format} ({start}).\033[0m")
                print(start + " ")
            else: 
                print("\033[31mWord not found. Break.\033[0m")
                break

    if start.endswith("."):
        dots += 1
        print()

#70 effective lines of code