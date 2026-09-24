import os

days_start = {f"Wochentag{i}": list() for i in range(1,6)}
days_end = {f"Wochentag{i}": list() for i in range(1,6)}
days_size = {f"Wochentag{i}": list() for i in range(1,6)}
days_value = {"Montag":1,"Dienstag":2,"Mittwoch":3,"Donnerstag":4,"Freitag":5,}
highest_val = 0

txtname = input("Wie heißt die Datei (ohne Dateiendung)?\n")

for dirpath, dirname, name in os.walk("."):
    for filename in name:
        if filename == (txtname + ".txt"):
            filepath = os.path.join(dirpath, filename)
            path = filepath

with open(path) as data:
    content = data.readlines()

for lines in content[1:]:

    values = lines.strip().split(" ")
    clazz, day, start, end, size = values
    days_start[f"Wochentag{days_value[day]}"].append(start)
    days_end[f"Wochentag{days_value[day]}"].append(end)
    days_size[f"Wochentag{days_value[day]}"].append(size)



