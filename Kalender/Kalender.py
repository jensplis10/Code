import json

task = ""


def new_termin():
    add_termin = {
        "name": input("Name\n"),
        "datum": input("Datum\n"),
        "beschreibung": input("Beschreibung\n"),
    }
    with open("termine.json", "r") as kalender:
        termin = json.load(kalender)
    termin.append(add_termin)
    with open("termine.json", "w") as kalender:
        json.dump(termin, kalender)


def del_termin():
    suche = input()
    if suche != "":
        with open("termine.json", "r") as kalender:
            termin = json.load(kalender)

        for i in range(0, len(termin)):
            if "name" in termin[i] and termin[i]["name"] == suche:
                termin[i] = {}
        with open("termine.json", "w") as kalender:
            json.dump(termin, kalender)


while task != 3:
    task = str
    while not task.isdigit() or task == "":
        task = input("Task\n")
    task = int

    if task == 1:
        new_termin()
    elif task == 2:
        del_termin()
