from time import sleep

while True:
    
    Zahl1 = input("Gib eine Zahl ein. ")
    Berechnen = input(
        "Möchtest du addieren subtrahieren multiplizieren oder dividieren? ")
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
    
