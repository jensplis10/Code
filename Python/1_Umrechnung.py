zehner = None
while zehner == None:
    zehnerString = input("Was ist die Zahl im Zehnersystem?\n")
    if zehnerString.isdigit():
        zehner = int(zehnerString)

system = None
while system == None:
    systemString = input("In welches System soll die Zahl umgewandelt werden?\n")
    if systemString.isdigit():
        system = int(systemString)

output = ""
while zehner != 0:
    output = output + str(zehner%system)
    zehner = int(zehner / system)

print(output[::-1])