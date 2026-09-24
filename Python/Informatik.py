zehner=int(input("Schreibe die Zahl des 10er Systems die umgerechnet werden soll.\n"))
system=int(input("In welches System soll die eingegebene Zahl umgewandelt werden?\n"))
print("\n")
Ergebniss=""
while zehner != 0:
    Ergebniss=Ergebniss+str(zehner%system)
    zehner=int(zehner/system)
print(Ergebniss[::-1]) 

