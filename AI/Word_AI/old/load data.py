import json
import anything
import tqdm
textinput_new = ""
filename = input("Filename: ")

with open("data2words.json", "r",encoding="utf-8") as data2words:
    data = json.load(data2words)



with open(filename+".txt","r",encoding="utf-8") as textinput_raw:
    textinput = textinput_raw.readlines()

for i in range(0,len(textinput)):
    textinput_new += textinput[i]
textinput_new = textinput_new.split()

for i in tqdm.tqdm(range(0,len(textinput_new)-2)):
    
    prefix = textinput_new[i] + " " + textinput_new[i+1]
    suffix = textinput_new[i+2]
    
    if {prefix:anything.Anything} in data:
        if {prefix:suffix} != data[data.index({prefix: anything.Anything})]:
            data[data.index({prefix: anything.Anything})] = {prefix:list(data[data.index({prefix: anything.Anything})].values())[0] + "/" + suffix}
    else:
        data.append({prefix:suffix})

with open("data2words.json", "w",encoding="utf-8") as data2words:
    json.dump(data, data2words)







textinput_new = ""

with open("data3words.json", "r",encoding="utf-8") as data3words:
    data = json.load(data3words)



with open(filename+".txt","r",encoding="utf-8") as textinput_raw:
    textinput = textinput_raw.readlines()

for i in range(0,len(textinput)):
    textinput_new += textinput[i]
textinput_new = textinput_new.split()

for i in tqdm.tqdm(range(0,len(textinput_new)-3)):
    
    prefix = textinput_new[i] + " " + textinput_new[i+1] + " " + textinput_new[i+2]
    suffix = textinput_new[i+3]
    
    if {prefix:anything.Anything} in data:
        if {prefix:suffix} != data[data.index({prefix: anything.Anything})]:
            data[data.index({prefix: anything.Anything})] = {prefix:list(data[data.index({prefix: anything.Anything})].values())[0] + "/" + suffix}
    else:
        data.append({prefix:suffix})

with open("data3words.json", "w",encoding="utf-8") as data3words:
    json.dump(data, data3words)








textinput_new = ""

with open("data4words.json", "r",encoding="utf-8") as data4words:
    data = json.load(data4words)



with open(filename+".txt","r",encoding="utf-8") as textinput_raw:
    textinput = textinput_raw.readlines()

for i in range(0,len(textinput)):
    textinput_new += textinput[i]
textinput_new = textinput_new.split()

for i in tqdm.tqdm(range(0,len(textinput_new)-4)):
    
    prefix = textinput_new[i] + " " + textinput_new[i+1] + " " + textinput_new[i+2] + " " + textinput_new[i+3]
    suffix = textinput_new[i+4]
    
    if {prefix:anything.Anything} in data:
        if {prefix:suffix} != data[data.index({prefix: anything.Anything})]:
            data[data.index({prefix: anything.Anything})] = {prefix:list(data[data.index({prefix: anything.Anything})].values())[0] + "/" + suffix}
    else:
        data.append({prefix:suffix})

with open("data4words.json", "w",encoding="utf-8") as data4words:
    json.dump(data, data4words)
