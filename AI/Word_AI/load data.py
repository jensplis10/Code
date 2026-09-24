import json
from collections import defaultdict
import tqdm
textinput = ""
filename = input("Filename: ")
wordasprefix = input("How many words as prefix? ")
filename_old = filename
books = 1

with open(f"AIDATA/datawords.json", "r",encoding="utf-8") as datawords:
    data = json.load(datawords)


while books < 10:
    filename = filename_old + str(books)
    textinput_new = ""


    for format in range(0,int(wordasprefix)-1):
        if format >= len(data):
            data.append({})
        data[format] = defaultdict(list)

        with open("AIDATA/"+filename+".txt","r",encoding="utf-8") as textinput_raw:
            textinput = textinput_raw.read().split()


        for i in tqdm.tqdm(range(0,len(textinput)-format-2)):
            
            prefix = " ".join(textinput[i:i+format+2])
            suffix = textinput[i+format+2]

            data[format][prefix].append(suffix)
    books += 1


with open(f"AIDATA/datawords.json", "w",encoding="utf-8") as datawords:
    json.dump(data, datawords)

#Die Chroniken von Araluen 0
