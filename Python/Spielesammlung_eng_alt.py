
print("Hey!")
input()
print("Do you want to speak 'Deutsch' or 'Englisch'? ")
Language = input()
if str(Language) == "Deutsch":
    print("Wie geht es dir? Super oder gut oder mittel oder schlecht?")
    Wie = input() 
    if str(Wie) == "Super":
        print("Das ist sehr gut. Möchtest du den Tachenrechner benutzen? Oder doch lieber ein Glücksspiel? Vielleicht ist heute dein Glückstag. Oder du möchtest entspannt ein Haus bauen? Alles ist möglich. Wenn du nach einem Spiel etwas anderes spielen möchtest gib einfach 'anderes' ein.")
        wel = input()
        from time import sleep
        from random import randint
        while True:
            if str(wel) == "Taschenrechner":
                Zahl1 = input("Gib eine Zahl ein. ")
                if str(Zahl1) == "anderes":
                    sleep(3)
                    print("\n")
                    break
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
                if str(Schwierigkeit) == "anderes":
                    sleep(3)
                    print("\n")
                    break
                elif str(Schwierigkeit) == "Leicht":
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
                eingabe2 = input()
                if str(eingabe2) == "anderes":
                    sleep(3)
                    print("\n")
                    break
                elif str(eingabe2) == "*":
                    rating = randint(6,10)
                    print("Dein Haus ist eine ",rating,"von 10. ")
                else:
                    sleep(1)
            else:
                print("Benutze Taschenrechner, Hausbauen oder Glücksspiel")
                sleep(3)
                break
        
    elif str(Wie) == "Gut":
        print("Das ist gut. Möchtest du den Tachenrechner benutzen? Oder doch lieber ein Glücksspiel? Vielleicht hast du Glück. Oder du möchtest entspannt ein Haus bauen? Alles ist möglich. Wenn du nach einem Spiel etwas anderes spielen möchtest gib einfach 'anderes' ein.")
        wel = input()
        from time import sleep
        from random import randint
        while True:
            if str(wel) == "Taschenrechner":
                Zahl1 = input("Gib eine Zahl ein. ")
                if str(Zahl1) == "anderes":
                    sleep(3)
                    print("\n")
                    break
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
                if str(Schwierigkeit) == "anderes":
                    sleep(3)
                    print("\n")
                    break
                elif str(Schwierigkeit) == "Leicht":
                    Raten = input("Ist ja easy. Rate eine Zahl von 1-10. ")
                    Zahl = randint(1,10)
                    if Zahl == str(Raten):
                        print("Du hast richtig geraten!")
                    else:
                        print("Verloren!")
                elif str(Schwierigkeit) == "Mittel":
                    Raten = input("Wagemutig, wagemutig. Rate eine Zahl von 1-100. ")
                    Zahl = randint(1,100)
                    if Zahl == str(Raten):
                        print("Du hast richtig geraten!")
                    else:
                        print("Verloren!")
                elif str(Schwierigkeit) == "Schwer":
                    Raten = input("Du willst es darauf ankommen lassen. Dann rate eine Zahl von 1-1000. ")
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
                eingabe2 = input()
                if str(eingabe2) == "*":
                    rating = randint(6,10)
                    print("Dein Haus ist eine ",rating,"von 10. ")
                elif str(eingabe2) == "anderes":
                    sleep(3)
                    print("\n")
                    break
                else:
                    sleep(1)
            else:
                print("Benutze Taschenrechner, Hausbauen oder Glücksspiel")
                sleep(3)
                break
            
    elif str(Wie) == "Mittel":
        print("Das ist nicht gut aber auch nicht schlecht. Ich werde dich ein bischen motivieren. Möchtest du den Tachenrechner benutzen? Oder doch lieber ein Glücksspiel? Vielleicht fühlst du dich nach einem Gewinn besser? Oder du möchtest entspannt ein Haus bauen? Alles ist möglich. Wenn du nach einem Spiel etwas anderes spielen möchtest gib einfach 'anderes' ein.")
        wel = input()
        from time import sleep
        from random import randint

        while True:
            if str(wel) == "Taschenrechner":
                Zahl1 = input("Gib eine Zahl ein. ")
                if str(Zahl1) == "anderes":
                    sleep(3)
                    print("\n")
                    break
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
                Schwierigkeit = input("Wähle die Schwierigkeit. Leicht oder mittel? ")
                if str(Schwierigkeit) == "anderes":
                    sleep(3)
                    print("\n")
                    break
                elif str(Schwierigkeit) == "Leicht":
                    Raten = input("Das geht ja noch. Rate eine Zahl von 1-10. ")
                    Zahl = randint(1,10)
                    if Zahl == str(Raten):
                        print("Du hast richtig geraten!")
                    else:
                        print("Verloren!")
                elif str(Schwierigkeit) == "Mittel":
                    Raten = input("Ein bischen tricky. Rate eine Zahl von 1-100. ")
                    Zahl = randint(1,100)
                    if Zahl == str(Raten):
                        print("Du hast richtig geraten!")
                    else:
                        print("Verloren!")
                        print("Die Zahl war",Zahl,".")
                sleep(3)
                print("\n")
            elif str(wel) == "Hausbauen":
                eingabe = input("Wilkommen bei bau dir ein Haus.Wenn du fertig bist drücke *. Dann werde ich dein Haus bewerten. Bitte drücke ENTER. ")
                eingabe2 = input()
                if str(eingabe2) == "*":
                    rating = randint(6,10)
                    print("Dein Haus ist eine ",rating,"von 10. ")
                elif str(eingabe2) == "anderes":
                    sleep(3)
                    print("\n")
                    break
                else:
                    sleep(1)
            else:
                print("Benutze Taschenrechner, Hausbauen oder Glücksspiel")
                sleep(3)
                break
    if str(Wie) == "Schlecht":
        print("Das ist schlecht. Vielleicht kann ich dich hiermit aufmuntern? Möchtest du den Tachenrechner benutzen? Oder doch lieber ein Glücksspiel? Es wird dir guttun wenn du gewinnst. Oder du möchtest entspannt ein Haus bauen? Alles ist möglich. Wenn du nach einem Spiel etwas anderes spielen möchtest gib einfach 'anderes' ein.")
        wel = input()
        from time import sleep
        from random import randint

        while True:
            if str(wel) == "Taschenrechner":
                Zahl1 = input("Gib eine Zahl ein. ")
                if str(Zahl1) == "anderes":
                    sleep(3)
                    print("\n")
                    break
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
                Raten = input("Du schaffst das. So schwer ist es nicht. Rate eine Zahl von 1-10. ")
                Zahl = randint(1,10)
                if str(Raten) == "anderes":
                    sleep(3)
                    print("\n")
                    break
                elif Zahl == str(Raten):
                    print("Du hast richtig geraten!")
                else:
                    print("Verloren!")
                    print("Die Zahl war",Zahl,".")
                sleep(3)
                print("\n")
            elif str(wel) == "Hausbauen":
                eingabe = input("Wilkommen bei bau dir ein Haus. Wenn du fertig bist drücke *. Dann werde ich dein Haus bewerten. Bitte drücke ENTER. ")
                eingabe2 = input()
                if str(eingabe2) == "anderes":
                    sleep(3)
                    print("\n")
                    break
                elif str(eingabe2) == "*":
                    rating = randint(6,10)
                    print("Dein Haus ist eine ",rating,"von 10. ")
                else:
                    sleep(1)
            else:
                print("Benutze Taschenrechner, Hausbauen oder Glücksspiel")
                sleep(3)
                break













































if str(Language) == "Englisch":
    print("How are you? Super or good or fine or bad?")
    Wie = input() 
    if str(Wie) == "Super":
        print("This is very good. Do you want to use a calculator? Or do you want to play a luck game? It could be that this is your lucky day. Or do you want to build a house? Everything is possible. If you want to play another gameafter you played a game enter 'else'.")
        wel = input()
        from time import sleep
        from random import randint
        while True:
            if str(wel) == "calculator":
                Zahl1 = input("Enter the first number. ")
                if str(Zahl1) == "else":
                    sleep(3)
                    print("\n")
                    break
                Berechnen = input("Möchtest du addieren subtrahieren multiplizieren oder dividieren? ")
                Zahl2 = input("Enter the second number. ")
                if str(Berechnen) == "+":
                    Ergebniss = int(Zahl1) + int(Zahl2)
                    print("The solution is ", (Ergebniss))
                elif str(Berechnen) == "-":
                    Ergebniss = int(Zahl1) - int(Zahl2)
                    print("The solution is ", (Ergebniss))
                elif str(Berechnen) == "*":
                    Ergebniss = int(Zahl1) * int(Zahl2)
                    print("The solution is ", (Ergebniss))
                elif str(Berechnen) == ":":
                    Ergebniss = int(Zahl1) / int(Zahl2)
                    print("The solution is ", (Ergebniss),".")
                else:
                    print("It didn't work.")
                sleep(3)
                print("\n")
            elif str(wel) == "luck game":
                Schwierigkeit = input("Choose the dufficulty. Easy, normal or hard? ")
                if str(Schwierigkeit) == "else":
                    sleep(3)
                    print("\n")
                    break
                elif str(Schwierigkeit) == "easy":
                    Raten = input("This is easy for you. Guess a number from 1-10. ")
                    Zahl = randint(1,10)
                    if Zahl == str(Raten):
                        print("That's right!")
                    else:
                        print("You lost!")
                elif str(Schwierigkeit) == "normal":
                    Raten = input("This could be a bit tricky. Guess a number from 1-100. ")
                    Zahl = randint(1,100)
                    if Zahl == str(Raten):("That's right!")
                    else:
                        print("You lost!")
                elif str(Schwierigkeit) == "hard":
                    Raten = input("Do you really want to do this? OK, guess a number from 1-1000. ")
                    Zahl = randint(1,1000)
                    if Zahl == str(Raten):
                        print("That's right!")
                    else:
                        print("You lost!")
                print("The number was",Zahl,".")
                sleep(3)
                print("\n")
            elif str(wel) == "housebuild":
                eingabe = input("Welcome to build your own house. If you're finished press *. Then I will rate your house. Please press ENTER. ")
                eingabe2 = input()
                if str(eingabe2) == "else":
                    sleep(3)
                    print("\n")
                    break
                elif str(eingabe2) == "*":
                    rating = randint(6,10)
                    print("Your house is",rating,"out of 10. ")
                else:
                    sleep(1)
            else:
                print("Use calculator, housebuild or luckgame")
                sleep(3)
                break
        
    elif str(Wie) == "good":
        print("This is good. Do you want to use a calculator? Or a luckgame? Today you could have luck. Or do you want to build a house? Everything is possible. If you want to play another game after you played a game enter 'else' .")
        wel = input()
        from time import sleep
        from random import randint
        while True:
            if str(wel) == "calculator":
                Zahl1 = input("Enter your first number. ")
                if str(Zahl1) == "else":
                    sleep(3)
                    print("\n")
                    break
                Berechnen = input("Möchtest du addieren subtrahieren multiplizieren oder dividieren? ")
                Zahl2 = input("Enter your second number. ")
                if str(Berechnen) == "+":
                    Ergebniss = int(Zahl1) + int(Zahl2)
                    print("The solution is ", (Ergebniss))
                elif str(Berechnen) == "-":
                    Ergebniss = int(Zahl1) - int(Zahl2)
                    print("The solution is ", (Ergebniss))
                elif str(Berechnen) == "*":
                    Ergebniss = int(Zahl1) * int(Zahl2)
                    print("The solution is ", (Ergebniss))
                elif str(Berechnen) == ":":
                    Ergebniss = int(Zahl1) / int(Zahl2)
                    print("The solution is ", (Ergebniss),".")
                else:
                    print("It didn't work")
                sleep(3)
                print("\n")
            elif str(wel) == "luckgame":
                Schwierigkeit = input("Choose the difficulty. Easy, normal or hard? ")
                if str(Schwierigkeit) == "else":
                    sleep(3)
                    print("\n")
                    break
                elif str(Schwierigkeit) == "easy":
                    Raten = input("This is easy. Guess a number from 1-10. ")
                    Zahl = randint(1,10)
                    if Zahl == str(Raten):
                        print("This is correct!")
                    else:
                        print("You lost!")
                elif str(Schwierigkeit) == "normal":
                    Raten = input("It's tricky. Guess a number from 1-100. ")
                    Zahl = randint(1,100)
                    if Zahl == str(Raten):
                        print("This is correct!")
                    else:
                        print("You lost!")
                elif str(Schwierigkeit) == "hard":
                    Raten = input("You want to try it? Then guess a number from 1-1000. ")
                    Zahl = randint(1,1000)
                    if Zahl == str(Raten):
                        print("This is correct!")
                    else:
                        print("You lost!")
                print("The number was",Zahl,".")
                sleep(3)
                print("\n")
            elif str(wel) == "housebuild":
                eingabe = input("Welcome to build your own house. If you're finished press *. Then I will rate your house from 1 to 10. Please press ENTER. ")
                eingabe2 = input()
                if str(eingabe2) == "*":
                    rating = randint(6,10)
                    print("Your house is a ",rating,"out of 10. ")
                elif str(eingabe2) == "else":
                    sleep(3)
                    print("\n")
                    break
                else:
                    sleep(1)
            else:
                print("Use calculator, housebuild or luckgame.")
                sleep(3)
                break
            
    elif str(Wie) == "fine":
        print("This isn't bad but it is also not good. I will motivate you. Do you want to use a calculator? Or a luckgame? You could feel better after a game? Or do you want to build a house? Everything is possible. If you want to play another game after you played a game enter 'else'.")
        wel = input()
        from time import sleep
        from random import randint

        while True:
            if str(wel) == "calculator":
                Zahl1 = input("Enter a number. ")
                if str(Zahl1) == "else":
                    sleep(3)
                    print("\n")
                    break
                Berechnen = input("Möchtest du addieren subtrahieren multiplizieren oder dividieren? ")
                Zahl2 = input("Enter a second number. ")
                if str(Berechnen) == "+":
                    Ergebniss = int(Zahl1) + int(Zahl2)
                    print("The solution is ", (Ergebniss))
                elif str(Berechnen) == "-":
                    Ergebniss = int(Zahl1) - int(Zahl2)
                    print("The solution is ", (Ergebniss))
                elif str(Berechnen) == "*":
                    Ergebniss = int(Zahl1) * int(Zahl2)
                    print("The solution is ", (Ergebniss))
                elif str(Berechnen) == ":":
                    Ergebniss = int(Zahl1) / int(Zahl2)
                    print("The solution is ", (Ergebniss),".")
                else:
                    print("It didn't work")
                sleep(3)
                print("\n")
            elif str(wel) == "luckgame":
                Schwierigkeit = input("Choose a difficulty. easy oder mittel? ")
                if str(Schwierigkeit) == "else":
                    sleep(3)
                    print("\n")
                    break
                elif str(Schwierigkeit) == "easy":
                    Raten = input("Das geht ja noch. Guess a number from 1-10. ")
                    Zahl = randint(1,10)
                    if Zahl == str(Raten):
                        print("That's right!")
                    else:
                        print("You lost!")
                elif str(Schwierigkeit) == "normal":
                    Raten = input("This is a bit tricky. Guess a number from 1-100. ")
                    Zahl = randint(1,100)
                    if Zahl == str(Raten):
                        print("That's right!")
                    else:
                        print("You lost!")
                        print("The number was",Zahl,".")
                sleep(3)
                print("\n")
            elif str(wel) == "housebuild":
                eingabe = input("Wilkommen bei bau dir ein Haus.Wenn du fertig bist drücke *. Dann werde ich dein Haus bewerten. Bitte drücke ENTER. ")
                eingabe2 = input()
                if str(eingabe2) == "*":
                    rating = randint(6,10)
                    print("Your house is a ",rating,"out of 10. ")
                elif str(eingabe2) == "else":
                    sleep(3)
                    print("\n")
                    break
                else:
                    sleep(1)
            else:
                print("Benutze calculator, housebuild or luckgame")
                sleep(3)
                break
    if str(Wie) == "bad":
        print("This is bad. Vielleicht kann ich dich hiermit aufmuntern? Do you want to use a calculator? Or a luckgame? Es wird dir guttun wenn du gewinnst. Oder du möchtest entspannt ein Haus bauen? Alles ist möglich. Wenn du nach einem Spiel etwas else spielen möchtest gib einfach 'else' ein.")
        wel = input()
        from time import sleep
        from random import randint

        while True:
            if str(wel) == "calculator":
                Zahl1 = input("Enter a number. ")
                if str(Zahl1) == "else":
                    sleep(3)
                    print("\n")
                    break
                Berechnen = input("Möchtest du addieren subtrahieren multiplizieren oder dividieren? ")
                Zahl2 = input("Enter a second number. ")
                if str(Berechnen) == "+":
                    Ergebniss = int(Zahl1) + int(Zahl2)
                    print("The solution is ", (Ergebniss))
                elif str(Berechnen) == "-":
                    Ergebniss = int(Zahl1) - int(Zahl2)
                    print("The solution is ", (Ergebniss))
                elif str(Berechnen) == "*":
                    Ergebniss = int(Zahl1) * int(Zahl2)
                    print("The solution is ", (Ergebniss))
                elif str(Berechnen) == ":":
                    Ergebniss = int(Zahl1) / int(Zahl2)
                    print("The solution is ", (Ergebniss),".")                
                else:
                    print("It didn't work.")
                    sleep(3)
                    print("\n") 
            elif str(wel) == "luckgame":
                Raten = input("You can do this. It isn't hard. Guess a number from 1-10. ")
                Zahl = randint(1,10)
                if str(Raten) == "else":
                    sleep(3)
                    print("\n")
                    break
                elif Zahl == str(Raten):
                    print("That's right!")
                else:
                    print("You lost!")
                    print("The number was",Zahl,".")
                sleep(3)
                print("\n")
            elif str(wel) == "Hausbauen":
                eingabe = input("Welcome to build your own house. If you're finished press *. Then I will rate your house. Please press ENTER. ")
                eingabe2 = input()
                if str(eingabe2) == "else":
                    sleep(3)
                    print("\n")
                    break
                elif str(eingabe2) == "*":
                    rating = randint(6,10)
                    print("Your house is a ",rating,"out of 10. ")
                else:
                    sleep(1)
            else:
                print("Use calculator, housebuild or luckgame")
                sleep(3)
                break

