eingabe = input("Wilkommen bei bau dir ein Haus.Wenn du fertig bist drücke *. Dann werde ich dein Haus bewerten. Bitte drücke ENTER. ")
from time import *
from random import * 
while True:
    eingabe2 = input()
    if str(eingabe2) == "*":
        rating = randint(1,10)
        print("Dein Haus ist eine ",rating,"von 10. ")
    else:
        sleep(1)

