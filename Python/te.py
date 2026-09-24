from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
)
import sys, re


def meineVerarbeitungsFunktion(zahl: str, system: str):
    global result, sehen
    system = int(system)

    zahl = str(zahl)
    potenz = 0
    output = 0
    chars = [char for char in str(zahl)]

    for char in reversed(chars):
        if char.isalpha():
            char1 = []
            char1.append(ord(char.upper()) - 55)
            char = int(*char1)
        output = int(output) + int(char) * system**potenz
        potenz = potenz + 1
    output1 = output
    output2 = output
    outputhex = ""
    while output1 != 0:
        if output1 % 16 >= 10:
            outputhex = outputhex + chr(output1 % 16 + 55)
        elif output1 % 16 < 10:
            outputhex = outputhex + str(output1 % 16)
        output1 = int(output1 / 16)

    outputbin = ""
    while output2 != 0:
        outputbin = outputbin + str(output2 % 2)
        output2 = int(output2 / 2)
    if system != 2 and system != 16:
        result = f"Die Zahl ist im Dezimalsystem {output}, im Binärsystem {outputbin[::-1]} und im Hexadezimalsystem {outputhex[::-1]}."
    elif system == 2:
        result = f"Die Zahl ist im Dezimalsystem {output} und im im Hexadezimalsystem {outputhex[::-1]}."
    elif system == 16:
        result = f"Die Zahl ist im Dezimalsystem {output} und im Binärsystem{outputbin[::-1]}."

    return result


def meineVerarbeitungsFunktion2(zehner: str, system2: str):
    global result, sehen
    system2 = int(system2)

    zehner = int(zehner)
    output = ""
    zehner1 = zehner
    zehner2 = zehner

    while zehner != 0:
        if zehner % system2 >= 10:
            output = output + chr(zehner % system2 + 55)
        elif zehner % system2 < 10:
            output = output + str(zehner % system2)
        zehner = int(zehner / system2)

    outputhex = ""
    while zehner1 != 0:
        if zehner1 % 16 >= 10:
            outputhex = outputhex + chr(zehner1 % 16 + 55)
        elif zehner1 % 16 < 10:
            outputhex = outputhex + str(zehner1 % 16)
        zehner1 = int(zehner1 / 16)

    outputbin = ""
    while zehner2 != 0:
        outputbin = outputbin + str(zehner2 % 2)
        zehner2 = int(zehner2 / 2)
    if system2 != 2 and system2 != 16:
        result = f"Die Zahl ist im {system2}er {output[::-1]}, im Binärsystem {outputbin[::-1]} und im Hexadezimalsystem {outputhex[::-1]}."
    elif system2 == 2:
        result = f"Die Zahl ist im Binärsystem {outputbin[::-1]} und im im Hexadezimalsystem {outputhex[::-1]}."
    elif system2 == 16:
        result = f"Die Zahl ist im Hexadezimalsystem {outputhex[::-1]} und im Binärsystem {outputbin[::-1]}."
    return result


def TRechnerver(zahl1):
    chars = [char for char in (zahl1)]
    Rechnung = ""
    for char in chars:
        if char.isdigit():
            Rechnung = str(Rechnung) + char
        elif char in {"+", "-", "/", "*", ":"}:
            if char == ":":
                char = "/"
            Rechnung = str(Rechnung) + char
        elif char.isalpha():
            print("Warning!")

    #    Rechnung=re.sub(r"[^\d\+\-\/\*\:]","",zahl1).replace(":","/")
    Ergebniss = eval(Rechnung)
    return f"Das Ergebniss ist {Ergebniss}."


def SystemDezimalsystem():
    global fenster
    fenster = QWidget()
    fenster.setWindowTitle("System -> Dezimalsystem")
    fenster.setGeometry(660, 465, 600, 150)

    eingabefeld = QLineEdit(fenster)
    eingabefeld.setPlaceholderText("Zahl im jeweiligen System")
    eingabefeld.move(50, 30)

    system = QLineEdit(fenster)
    system.setPlaceholderText("System")
    system.move(50, 60)

    label = QLabel(fenster)
    label.move(50, 120)
    label.setText("")
    label.setMinimumWidth(1000)

    button = QPushButton(fenster)
    button.move(50, 90)
    button.setText("Bestätigen")

    button.clicked.connect(
        lambda x: label.setText(
            str(meineVerarbeitungsFunktion(eingabefeld.text(), system.text()))
        )
    )
    fenster.show()


def DezimalsystemSystem():
    global fenster2
    fenster2 = QWidget()
    fenster2.setWindowTitle("Dezimalsystem -> System")
    fenster2.setGeometry(660, 465, 600, 150)

    zehner = QLineEdit(fenster2)
    zehner.setPlaceholderText("Zahl im Dezimalsystem")
    zehner.move(50, 30)

    system2 = QLineEdit(fenster2)
    system2.setPlaceholderText("System in das umgewandelt werden soll")
    system2.move(50, 60)

    label2 = QLabel(fenster2)
    label2.move(50, 120)
    label2.setText("")
    label2.setMinimumWidth(1000)

    button2 = QPushButton(fenster2)
    button2.move(50, 90)
    button2.setText("Bestätigen")

    button2.clicked.connect(
        lambda x: label2.setText(
            str(meineVerarbeitungsFunktion2(zehner.text(), system2.text()))
        )
    )
    fenster2.show()


def TRechner():
    global fenster3

    fenster3 = QWidget()
    fenster3.setWindowTitle("Taschenrechner")
    fenster3.setGeometry(810, 465, 300, 100)

    zahl1 = QLineEdit(fenster3)
    zahl1.setPlaceholderText("Rechnung eingeben")
    zahl1.move(10, 25)

    label3 = QLabel(fenster3)
    label3.move(10, 75)
    label3.setText("")
    label3.setMinimumWidth(1000)

    button3 = QPushButton(fenster3)
    button3.move(10, 50)
    button3.setText("Bestätigen")

    button3.clicked.connect(lambda x: label3.setText(str(TRechnerver(zahl1.text()))))
    fenster3.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    sehen = QWidget()
    sehen.resize(300, 150)
    sehen.setWindowTitle("Umrechnung")

    button3 = QPushButton(sehen)
    button3.move(10, 25)
    button3.setText("System -> Dezimalsystem")

    button3.clicked.connect(SystemDezimalsystem)

    button4 = QPushButton(sehen)
    button4.move(10, 75)
    button4.setText("Dezimalsystem -> System")

    button4.clicked.connect(DezimalsystemSystem)

    button5 = QPushButton()
    button5.move(10, 125)
    button5.setText("Taschenrechner")

    button5.clicked.connect(TRechner)

    layout = QVBoxLayout(sehen)
    layout.addWidget(button3)
    layout.addWidget(button4)
    layout.addWidget(button5)

    sehen.show()
    sys.exit(app.exec_())
