from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout
import sys,re
def meineVerarbeitungsFunktion(eingabefeld:str,system:str,system2):
    global  result,sehen
    system=int(system)
    system2=int(system2)

    eingabefeld=str(eingabefeld)
    potenz = 0
    output = 0
    chars = [char for char in str(eingabefeld)]
    
    for char in reversed(chars):
        if char.isalpha():
            char1=[]
            char1.append(ord(char.upper()) -55)
            char =int(*char1) 
        output =(int(output) + int(char) * system ** potenz)
        potenz = potenz + 1
    zehnerhex=output
    zehnerbin=output
    outputdez=output
    zehner=output
    outputhex = ""
    while zehnerhex != 0:
        if zehnerhex%16>=10:
            outputhex=outputhex+chr(zehnerhex%16+55)                                           
        elif zehnerhex%16 <10:
            outputhex = outputhex + str(zehnerhex%16)
        zehnerhex = int(zehnerhex / 16)
    output=""
    while zehner != 0:
        if zehner%system2>=10:
            output=output+chr(zehner%system2+55)                                           
        elif zehner%system2 <10:
            output = output + str(zehner%system2)
        zehner = int(zehner / system2)

    outputbin = ""
    while zehnerbin != 0:                                         
        outputbin = outputbin + str(zehnerbin%2)
        zehnerbin = int(zehnerbin / 2)
    if system!=2 and system2!=2 and system!=16 and system2!=16 and system!=10 and system2!=10:
        result=(f"Die Zahl ist im {system2}er {output[::-1]}. Im Dezimalsystem {outputdez}, im Binärsystem {outputbin[::-1]} und im Hexadezimal {outputhex[::-1]}.")
    elif system2 == 2:
        result =(f"Die Zahl ist im Binärsystem {outputbin[::-1]}, im Dezimalsystem {outputdez} und im im Hexadezimalsystem {outputhex[::-1]}.")
    elif system2 == 16:
        result =(f"Die Zahl ist im Hexadezimalsystem {outputhex[::-1]}, im Dezimalsystem {outputdez} und im Binärsystem {outputbin[::-1]}.")
    elif system2 == 10:
        result =(f"Die Zahl ist im Dezimalsystem {outputdez}, ist im Hexadezimalsystem {outputhex[::-1]} und im Binärsystem {outputbin[::-1]}.")
    elif system==10:
        result=(f"Die Zahl ist im {system2}er {output[::-1]}. Im Binärsystem {outputbin[::-1]} und im Hexadezimal {outputhex[::-1]}.")
    elif system==2:
        result=(f"Die Zahl ist im {system2}er {output[::-1]}. Im Dezimalsystem {outputdez} und im Hexadezimal {outputhex[::-1]}.")
    elif system==16:
        result=(f"Die Zahl ist im {system2}er {output[::-1]}. Im Dezimalsystem {outputdez} und im Binärsystem {outputbin[::-1]}.")
    return(result)
    
        


def meineTaschenrechnerfunktion(eingabefeld:str,system:str):
    system=int(system)

    eingabefeld=str(eingabefeld)
    potenz = 0
    output = 0
    chars = [char for char in str(eingabefeld)]
    
    for char in chars:
        if char.isalpha():
            char1=[]
            char1.append(ord(char.upper()) -55)
            char =int(*char1) 
            output =(str(output) + char * system ** potenz)
            potenz = potenz + 1
        elif char.isdigit():
            output =(str(output) + char * system ** potenz)
            potenz = potenz + 1
        elif char in {"+","-","/","*",":"}:
            output=str(output)+str(char)

    chars=[char for char in (output)]
    Rechnung=""
    for char in chars:
        if char.isdigit():
            Rechnung=str(Rechnung)+char
        elif char in {"+","-","/","*",":"}:
            if char==":":
                char="/"
            Rechnung=str(Rechnung)+char
        elif char.isalpha():
            print("Warning!")

    zehner=eval(Rechnung)
    output=""
    while zehner != 0:
        if zehner%system>=10:
            output=output+chr(zehner%system+55)                                           
        elif zehner%system <10:
            output = output + str(zehner%system)
        zehner = int(zehner / system)
    return(output)


def TRechnerver(zahl1):
    chars=[char for char in (zahl1)]
    Rechnung=""
    for char in chars:
        if char.isdigit():
            Rechnung=str(Rechnung)+char
        elif char in {"+","-","/","*",":"}:
            if char==":":
                char="/"
            Rechnung=str(Rechnung)+char
        elif char.isalpha():
            print("Warning!")
    
#    Rechnung=re.sub(r"[^\d\+\-\/\*\:]","",zahl1).replace(":","/")
    Ergebniss=eval(Rechnung)
    return(f"Das Ergebniss ist {Ergebniss}.")

def SystemSystem():
    global fenster
    fenster = QWidget()
    fenster.setWindowTitle("System -> System")
    fenster.setGeometry(660, 465, 600, 150)

    eingabefeld = QLineEdit(fenster)
    eingabefeld.setPlaceholderText("Zahl im jeweiligen System")
    eingabefeld.move(50, 25)  

    system = QLineEdit(fenster)
    system.setPlaceholderText("System")
    system.move(50, 50)  

    system2 = QLineEdit(fenster)
    system2.setPlaceholderText("System in das umgewandelt werden soll")
    system2.move(50, 75)  

    label=QLabel(fenster)
    label.move(50,125)
    label.setText("")
    label.setMinimumWidth(1000)

    button = QPushButton(fenster)
    button.move(50,100)
    button.setText("Bestätigen")

    button.clicked.connect(lambda x: label.setText(str(meineVerarbeitungsFunktion(eingabefeld.text(),system.text(),system2.text()))))
    fenster.show()

def TaschenrechnerSystem():
    global fenster
    fenster = QWidget()
    fenster.setWindowTitle("Taschenrechner Systeme")
    fenster.setGeometry(660, 465, 600, 150)

    eingabefeld = QLineEdit(fenster)
    eingabefeld.setPlaceholderText("Zahl im jeweiligen System")
    eingabefeld.move(50, 25)  

    system = QLineEdit(fenster)
    system.setPlaceholderText("System")
    system.move(50, 50)  

    label=QLabel(fenster)
    label.move(50,125)
    label.setText("")
    label.setMinimumWidth(1000)

    button = QPushButton(fenster)
    button.move(50,100)
    button.setText("Bestätigen")

    button.clicked.connect(lambda x: label.setText(str(meineTaschenrechnerfunktion(eingabefeld.text(),system.text()))))
    fenster.show()

def TRechner():
    global fenster3

    fenster3 =QWidget()
    fenster3.setWindowTitle("Taschenrechner")
    fenster3.setGeometry(810,465,300,100)

    zahl1=QLineEdit(fenster3)
    zahl1.setPlaceholderText("Rechnung eingeben")
    zahl1.move(10, 25) 

    label3=QLabel(fenster3)
    label3.move(10,75)
    label3.setText("")
    label3.setMinimumWidth(1000)

    button3 = QPushButton(fenster3)
    button3.move(10,50)
    button3.setText("Bestätigen")

    button3.clicked.connect(lambda x: label3.setText(str(TRechnerver(zahl1.text()))))
    fenster3.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    sehen = QWidget()
    sehen.resize(300, 100)
    sehen.setWindowTitle("Umrechnung")

    button3 = QPushButton(sehen)
    button3.move(10,25)
    button3.setText("System -> System")

    button3.clicked.connect(SystemSystem)

    button4 = QPushButton(sehen)
    button4.move(10,50)
    button4.setText("Taschenrechner Systeme")

    button4.clicked.connect(TaschenrechnerSystem)

    button5=QPushButton()
    button5.move(10,75)
    button5.setText("Taschenrechner")

    button5.clicked.connect(TRechner)

    layout = QVBoxLayout(sehen)
    layout.addWidget(button3)
    layout.addWidget(button4)
    layout.addWidget(button5)

    sehen.show()
    sys.exit(app.exec_())


