
wiederholen=""
while umrechnung.upper() != "STOP":
    umrechnung=input("Soll vom Dezimalsystem in ein anderes System (D) oder von einem System ins Dezimalsystem (S) umgewandelt werden. Wenn du das Programm beenden willst gebe einfach 'Stop' ein.\n") 
    if str(umrechnung)== "D":
        wiederholen = ""
        while wiederholen.upper != "STOP":
            zehner = None
            while zehner == None:
                zehnerString = input("Was ist deine Zahl im Dezimalsystem?\n")
                if zehnerString.upper()=="STOP":
                    break
                elif zehnerString.isdigit():
                    zehner = int(zehnerString)
            if zehnerString.upper()=="STOP":
                break
            system = None
            while system == None:
                systemString = input("In welches System soll die Zahl umgewandelt werden?\n")
                if systemString.upper()=="STOP":
                    break
                elif systemString.isdigit():
                    system = int(systemString)
            if systemString.upper()=="STOP":
                break
            output = ""
            zehner1=zehner
            zehner2=zehner
            
            while zehner != 0:
                if zehner%system>=10:
                    output=chr(zehner%system+55)                                           
                elif zehner%system <10:
                    output = output + str(zehner%system)
                zehner = int(zehner / system)

            output1 = ""
            while zehner1 != 0:
                if zehner1%16>=10:
                    output1=chr(zehner1%16+55)                                           
                elif zehner1%16 <10:
                    output1 = output1 + str(zehner1%16)
                zehner1 = int(zehner1 / 16)

            output2 = ""
            while zehner2 != 0:                                         
                output2 = output2 + str(zehner2%2)
                zehner2 = int(zehner2 / 2)
            if system!=2 and system!=16:
                print("Die Zahl ist im",system,"er System",output[::-1])
                print("Die Zahl ist im Binärsystem",output2[::-1])
                print("Die Zahl ist im Hexadezimalsystem",output1[::-1])
            elif system == 2:
                print("Die Zahl ist im Binärsystem",output2[::-1])
                print("Die Zahl ist im Hexadezimalsystem",output1[::-1])
            elif system == 16:
                print("Die Zahl ist im Hexadezimalsystem",output1[::-1])
                print("Die Zahl ist im Binärsystem",output2[::-1])
            wiederholen=input("Soll neu gestartet werder(ENTER)? Sonst gib einfach 'Stop' ein.\n")
            if wiederholen.upper()=="STOP":
                break




    elif str(umrechnung)=="S":    
        wiederholen = ""
        while wiederholen.upper != "STOP":
            system = None
            while system == None:
                systemString = input("Von welchem System soll eine Zahl umgewandelt werden?\n")
                if systemString.upper()=="STOP":
                    break
                elif systemString.isdigit():                  
                    system = int(systemString)
            if systemString.upper()=="STOP":
                break
            zahl= input(f"Was ist die Zahl im {system}er System?\n")
            if zahl.upper()=="STOP":
                break
            zahl=str(zahl)
            potenz = 0
            output = 0
            chars = [char for char in str(zahl)]
            print("\n")
            
            for char in reversed(chars):
                if char.isalpha():
                    char1=[]
                    char1.append(ord(char.upper()) -55)
                    char =int(*char1)
                    print(char) 
                output =(int(output) + int(char) * system ** potenz)
                potenz = potenz + 1
            output1=output
            output2=output
            outputhex = ""
            while output1 != 0:
                if output1%16>=10:
                    outputhex=chr(output1%16+55)                                           
                elif output1%16 <10:
                    outputhex = outputhex + str(output1%16)
                output1 = int(output1 / 16)

            outputbin = ""
            while output2 != 0:                                         
                outputbin = outputbin + str(output2%2)
                output2 = int(output2 / 2)
            if system!=2 and system!=16:
                print("Die Zahl ist im Dezimalsystem",output)
                print("Die Zahl ist im Binärsystem",outputbin[::-1])
                print("Die Zahl ist im Hexadezimalsystem",outputhex[::-1])
            elif system == 2:
                print("Die Zahl ist im Dezimalsystem",output)
                print("Die Zahl ist im Hexadezimalsystem",outputhex[::-1])
            elif system == 16:
                print("Die Zahl ist im Dezimalsystem",output)
                print("Die Zahl ist im Binärsystem",outputbin[::-1])
            wiederholen=input("Soll neu gestartet werder(ENTER)? Sonst gib einfach 'Stop' ein.\n")
            if wiederholen.upper()=="STOP":
                break
exit()



