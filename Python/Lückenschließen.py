from random import *
from time import *
import time
while True:
    zeit=time.time()
    print("Schließe die Lücken indem du die passende Zahl angibst. Du musst aber schnell sein.")
    zahl= randint(1,100)
    zahl2= zahl+2
    print(zahl,"___",zahl2)
    zahl3=input("")
    zeit2=time.time()
    if zeit2-zeit>10:
        print("Zu langsam.")
    elif (zahl2-1)==int(zahl3):
        print("Richtig")
        print("Du hast",zeit2-zeit,"Sekunden gebraucht.")
    
    else:
        print("Falsch")
        print("Die Zahl war",zahl+1)
        