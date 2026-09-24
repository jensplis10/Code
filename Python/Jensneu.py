from random import *
from time import sleep
while True:
    Schwierigkeit = input("Wähle die Schwierigkeit. Leicht, mittel oder schwer? ")
    if str(Schwierigkeit) == "Leicht":
        Raten = input("Rate eine Zahl von 1-10. ")
        Zahl = randint(1,10)
        if Zahl == str(Raten):
            print("Du hast richtig geraten!")
        else:
            print("Verloren!")
    if str(Schwierigkeit) == "Mittel":
        Raten = input("Rate eine Zahl von 1-100. ")
        Zahl = randint(1,100)
        if Zahl == str(Raten):
            print("Du hast richtig geraten!")
        else:
            print("Verloren!")
    if str(Schwierigkeit) == "Schwer":
        Raten = input("Rate eine Zahl von 1-1000. ")
        Zahl = randint(1,1000)
        if Zahl == str(Raten):
            print("Du hast richtig geraten!")
        else:
            print("Verloren!")
    print("Die Zahl war",Zahl,".")
    sleep(3)
    print("\n")



