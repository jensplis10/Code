import re

listnumber = 1
index = 1
list_dict = {f"{i}er": str() for i in range(1, 10)}


def finPar(rec):
    parts = re.findall(r"\d+|[+]", rec)
    return parts


def sort(parts):
    out = []
    zwS = []

    for part in parts:
        if part.isdigit():
            out.append(int(part))
        elif part == "+":
            if zwS != []:
                out.append(zwS.pop())
            zwS.append(part)
    while zwS:
        out.append(zwS.pop())
    return out


def solve(rRF):
    zwS = []

    for part in rRF:
        if isinstance(part, int):
            zwS.append(part)
        else:
            if len(rRF) > 2:
                y = zwS.pop()
                x = zwS.pop()

                if part == "+":
                    zwS.append(x + y)
    return zwS[0]


# Stoppt wenn sie einen Buchstaben eingeben.
# Ansonsten immer ENTER eingeben
while input("\n") == "":
    listnumber = 1
    # Schüler müssen hier ihre Zahlen eingeben
    # Es gibt eine Sicherung dass wenn sie einen Buchstaben eingeben oder etwas anderes außer eine Zahl dass sie dann direkt nochmal eingeben müssen
    while listnumber != 10:
        inp = ""
        while not inp.isdigit():
            inp = input(f"Gebe die Anzahl von {listnumber}ern an\n")
        list_dict[f"{listnumber}er"] += inp
        list_dict[f"{listnumber}er"] += "+"
        listnumber += 1

for i in range(1, 10):
    list_dict[f"{i}er"] += "0"

for i in range(1, 10):

    rec = list_dict[f"{i}er"]
    parts = finPar(rec)
    rRF = sort(parts)
    erg = solve(rRF)
    print(f"Es gibt {erg} {i}er")

while index != 10:
    rec += list_dict[f"{index}er"]
    rec += "+"
    index += 1

rec += "0"

parts = finPar(rec)
rRF = sort(parts)
erg = solve(rRF)
print(f"\nEs gibt insgesamt {erg} Werte")
