output = []

def remove_until_punctuation(eingabe):
    eingabe = eingabe[:-2]
    while eingabe and eingabe[-1] not in ".?!":
        eingabe = eingabe[:-1]
    return eingabe

with open("germantoenglisch.txt", "r",encoding="utf-8") as germantoenglisch:
    data = germantoenglisch.readlines()
for i in range(0,len(data)):
    output.append(remove_until_punctuation(data[i]))

with open("germantoenglischfinish.txt", "w",encoding="utf-8") as germantoenglischfinish:
    germantoenglischfinish.write(str(output))