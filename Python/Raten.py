from random import *
from time import *
Computer=input("Möchtest du 1. den Zahlenbereich selber wählen und deine Versuche auch\noder 2. soll der Computer das entscheiden? Gebe 1 ein für die erste Option oder 2 für die zweite Option.\n")
if int(Computer)==1:
    Spielraum=int(input("Wähle die höchste Zahl im Zahlenbereich.\n"))
    Versuche=int(input("Wie viele Versuche möchtest du haben.\n"))
    Zahl=randint(1,Spielraum)
elif int(Computer)==2:
    Spielraum=randint(10,100)
    Versuche= int(Spielraum/3)
    Zahl=randint(1,Spielraum)
print("Rate die ausgedachte Zahl die sich in einem Zahlenbereich von 1 -",Spielraum,"befindet.")
print("Du hast",Versuche,"Versuche.")
for variable in range(0,Versuche):
    raten=input()
    if int(raten)==int(Zahl):
        print("Du hast gewonnen!")
    elif int(raten) - int(Zahl) >0:
        print("Du hast noch",Versuche-variable-1,"Versuche übrig. Die gesuchte Zahl ist kleiner.")
        
    elif int(raten) - int(Zahl) <0:
        print("Du hast noch",Versuche-variable-1,"Versuche übrig. Die gesuchte Zahl ist größer.")
        
    elif int(raten) > int(Spielraum):
        print("Du kannst nur Zahlen von 1 -",Spielraum,"eingeben")
        print("Du hast noch",Versuche-variable-1,"Versuche übrig.")
    else:
        print("Gebe bitte gerade Zahlen ein.")
        print("Du hast noch",Versuche-variable-1,"Versuche übrig.")
print("Du hast verloren du Looser. Die richtige Zahl war",Zahl)
