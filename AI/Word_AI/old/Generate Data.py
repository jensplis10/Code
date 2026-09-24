import json
import random
import anything 
import sys
dots = 0
format = int(input("Format: "))
with open(f"data{format}words.json", "r", encoding="utf-8") as ai:
    data = json.load(ai)
start = input(f"Please enter {format} words.\n")
sentence = int(input("How many sentences?\n"))

while dots < sentence:
    if {start:anything.Anything} in data:
        if not "/" in list(data[data.index({start:anything.Anything})].values())[0]:
            sys.stdout.write(list(data[data.index({start: anything.Anything})].values())[0] + " ")
            words = ""
            for word in list(data[data.index({start: anything.Anything})])[0].split():
                if word != list(data[data.index({start: anything.Anything})])[0].split()[0]:
                    words += word + " "
            start = words + list(data[data.index({start: anything.Anything})].values())[0]
        else:
            word_search = list(data[data.index({start: anything.Anything})].values())[0].split("/")
            word_search = [word for word in word_search if word != ""]
            new_word = word_search[random.randint(0,len(word_search)-1)]
            sys.stdout.write(new_word + " ")
            words = ""
            for word in list(data[data.index({start: anything.Anything})])[0].split():
                if word != list(data[data.index({start: anything.Anything})])[0].split()[0]:
                    words += word + " "
            start = words + new_word
    else:
        if format > 2:
            format -= 1
            with open(f"data{format}words.json", "r", encoding="utf-8") as ai:
                data = json.load(ai)
            while not start.endswith(" "):
                start = start[:-1]
            start = start[:-1]
            print(f"Word not found. Switched to Format {format}. Deacreased words to {format} ({start}).")
            sys.stdout.write(start + " ")
        else: 
            print("Word not found. Break.")
            break
    if start.endswith("."):
        dots += 1
        print()