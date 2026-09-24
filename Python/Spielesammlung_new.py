from time import sleep
from random import *

print("Hey!")
input()
print("Wie geht es dir? Super oder gut oder mittel oder schlecht?")
Wie = input() 
if str(Wie) == "Super":
    print("Das ist sehr gut. Möchtest du den Tachenrechner benutzen? Oder doch lieber ein Glücksspiel? Vielleicht ist heute dein Glückstag. Oder du möchtest entspannt ein Haus bauen? Alles ist möglich. Wenn du etwas anderes spielen möchtest gib einfach 'anderes' ein.")
elif str(Wie) == "Gut":
    print("Das ist gut. Möchtest du den Tachenrechner benutzen? Oder doch lieber ein Glücksspiel? Vielleicht hast du Glück. Oder du möchtest entspannt ein Haus bauen? Alles ist möglich. Wenn du etwas anderes spielen möchtest gib einfach 'anderes' ein.")
elif str(Wie) == "Mittel":
    print("Das ist nicht gut aber auch nicht schlecht. Ich werde dich ein bischen motivieren. Möchtest du den Tachenrechner benutzen? Oder doch lieber ein Glücksspiel? Vielleicht fühlst du dich nach einem Gewinn besser? Oder du möchtest entspannt ein Haus bauen? Alles ist möglich. Wenn du etwas anderes spielen möchtest gib einfach 'anderes' ein.")
elif str(Wie) == "Schlecht":
    print("Das ist schlecht. Vielleicht kann ich dich hiermit aufmuntern? Möchtest du den Tachenrechner benutzen? Oder doch lieber ein Glücksspiel? Es wird dir guttun wenn du gewinnst. Oder du möchtest entspannt ein Haus bauen? Alles ist möglich. Wenn du etwas anderes spielen möchtest gib einfach 'anderes' ein.")
else:
    print("Möchtest du den Tachenrechner benutzen? Oder doch lieber ein Glücksspiel? Vielleicht ist heute dein Glückstag. Oder du möchtest entspannt ein Haus bauen? Alles ist möglich. Wenn du etwas anderes spielen möchtest gib einfach 'anderes' ein.")

wel = input()
while True:
    if str(wel) == "Taschenrechner":
        Zahl1 = input("Gib eine Zahl ein. ")
        Berechnen = input("Möchtest du addieren subtrahieren multiplizieren oder dividieren? ")
        Zahl2 = input("Gib eine zweite Zahl ein. ")
        if str(Berechnen) == "+":
            Ergebniss = int(Zahl1) + int(Zahl2)
            print("Das Ergebniss lautet ", (Ergebniss))
        elif str(Berechnen) == "-":
            Ergebniss = int(Zahl1) - int(Zahl2)
            print("Das Ergebniss lautet ", (Ergebniss))
        elif str(Berechnen) == "*":
            Ergebniss = int(Zahl1) * int(Zahl2)
            print("Das Ergebniss lautet ", (Ergebniss))
        elif str(Berechnen) == ":":
            Ergebniss = int(Zahl1) / int(Zahl2)
            print("Das Ergebniss lautet ", (Ergebniss),".")
        else:
            print("Es hat nicht funktioniert")    
        sleep(3)
        print("\n")
    elif str(wel) == "Glücksspiel":
        Schwierigkeit = input("Wähle die Schwierigkeit. Leicht, mittel oder schwer? ")
        if str(Schwierigkeit) == "Leicht":
            Raten = input("Ist ja easy für nen Glückspilz wie dich. Das machst du mit links. Rate eine Zahl von 1-10. ")
            Zahl = randint(1,10)
            if Zahl == str(Raten):
                print("Du hast richtig geraten!")
            else:
                print("Verloren!")
        elif str(Schwierigkeit) == "Mittel":
            Raten = input("Das ist wagemutig. Rate eine Zahl von 1-100. ")
            Zahl = randint(1,100)
            if Zahl == str(Raten):
                print("Du hast richtig geraten!")
            else:
                print("Verloren!")
        elif str(Schwierigkeit) == "Schwer":
            Raten = input("Du willst es darauf ankommen lassen? OK, rate eine Zahl von 1-1000. ")
            Zahl = randint(1,1000)
            if Zahl == str(Raten):
                print("Du hast richtig geraten!")
            else:
                print("Verloren!")
        print("Die Zahl war",Zahl,".")
        sleep(3)
        print("\n")
    elif str(wel) == "Hausbauen":
        eingabe = input("Wilkommen bei bau dir ein Haus.Wenn du fertig bist drücke *. Dann werde ich dein Haus bewerten. Bitte drücke ENTER. ")
        while True:
            eingabe2 = input()
            if str(eingabe2) == "*":
                rating = randint(6,10)
                print("Dein Haus ist eine ",rating,"von 10. ")
                break
            else:
                sleep(1)
    elif str(Zahl1) == "anderes":            
        sleep(3)
        print("\n")
    elif str(Raten) == "anderes":            
        sleep(3)
        print("\n")
    elif str(eingabe) == "anderes":            
        sleep(3)
        print("\n")
    else:
        print("Benutze Taschenrechner, Hausbauen oder Glücksspiel")
