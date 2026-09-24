umrechnung="test"
while umrechnung != "":
    umrechnung=input("Soll vom Dezimalsystem in ein anderes System (D) oder von einem System ins Dezimalsystem (S) umgewandelt werden. Wenn du das Programm beenden willst drücke(ENTER).\n")
    if str(umrechnung)== "D":
        wiederholen = ""
        while wiederholen == "":
            zehner = None
            while zehner == None:
                zehnerString = input("Was ist deine Zahl im Dezimalsystem?\n")
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
            print("Die Zahl ist im",system,"er System",output[::-1])
            wiederholen=input("Soll neu gestartet werder(ENTER)? Sonst gib einfach etwas ein.\n")
    elif str(umrechnung)=="S":    
        wiederholen = ""
        while wiederholen == "":
            system = None
            while system == None:
                systemString = input("Von welchem System soll eine Zahl umgewandelt werden?\n")
                if systemString.isdigit():                  
                    system = int(systemString)
            zahl = None
            while zahl == None:
                zahlString = input(f"Was ist die Zahl im {system}er System?\n")
                if zahlString.isdigit():
                    zahl = int(zahlString)
            potenz = 0
            output = 0
            chars = [char for char in str(zahl)]
            print("\n")
            for char in reversed(chars):
                output =(int(output) + int(char) * system ** potenz)
                potenz = potenz + 1
            print("Die Zahl ist im Dezimalsystem",output)
            wiederholen=input("Soll neu gestartet werder(ENTER)? Sonst gib einfach etwas ein.\n")
exit()