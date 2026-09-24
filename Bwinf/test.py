import os

txtname = input("Wie heißt die Datei (ohne Dateiendung)?\n")
days = []
starttimes = []
endtimes = []
sizeall = []
ballscopy = []
timecopy = []
balls = 0

for dirpath, dirname, name in os.walk("."):
    for filename in name:
        if filename == (txtname + ".txt"):
            filepath = os.path.join(dirpath, filename)
            path = filepath

with open(path) as data:
    content = data.readlines()

for lines in content[1:]:

    values = lines.split(" ")
    clazz, day, start, end, size = values

    balls = size
    time = day + " um " + start

    sizeall.append(int(size))
    days.append(day)
    ballscopy.append(int(balls))
    timecopy.append(time)
    starttimes.append(int(start))
    endtimes.append(int(end))

for zeichen in range(0, len(sizeall) - 1):
    if (
        days[zeichen] == day
        and (int(start) < endtimes[zeichen])
        and (int(end) > starttimes[zeichen])
    ):
        if int(balls) < ((int(ballscopy[zeichen]) + int(size))):
            balls = int(ballscopy[zeichen]) + int(size)
            ballscopy[zeichen] = int(balls)
            time = day + " um " + str(max(int(start), int(starttimes[zeichen])))
            timecopy[zeichen] = time

balls = max(ballscopy)
time = timecopy[ballscopy.index(max(ballscopy))]
print("Es werden", int(balls), "am", time, "Uhr benötigt.")
