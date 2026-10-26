Stand: 1.9.2026
---------------
In dieser Aufgabe geht es um komplette Pizzen. Auf denen sind – außer Tomatensauce und Käse natürlich – zwei Sorten Beläge: laut Aufgabe entweder Thunfisch oder Spinat, aber auch andere Sorten sind denkbar. Für die Lösung ist wichtig, wo genau die einzelnen Beläge – also die Häufchen von Thunfisch oder Spinat, die Pilzstücke, die Salamischeiben usw. liegen. Zur Vereinfachung ist die Pizza immer ein Kreis um den Nullpunkt (0 | 0) des Koordinatensystems, und die einzelnen Beläge werden als Vielecke beschrieben.
Zu dieser Aufgabe gibt es 8 Beispieleingaben:
    • halb00.txt
    • halb01.txt
    • halb02.txt
    • halb03.txt
    • halb04.txt
    • halb05.txt
    • halb06.txt
    • halb07.txt

Jede Datei beschreibt eine Pizza und ist so aufgebaut:
    • 1. Zeile: Der Radius r der Pizza.
    • 2. Zeile: Die Anzahl n der Beläge der ersten Sorte.
    • Jede der folgenden n Zeilen beschreibt einen Belag als Vieleck und enthält nacheinander
        ◦ die Anzahl der Ecken des Vielecks und
        ◦ für jeden Eckpunkt des Vielecks dessen x- und y-Koordinaten. 
(Die Eckpunkte werden gegen den Uhrzeigersinn angegeben.)
    • Zeile n+3: Die Anzahl m der Beläge der zweiten Sorte. 
    • Jede der folgenden m Zeilen beschreibt einen Belag als Vieleck, wie bei der ersten Sorte.

Hier ist eine Beispieleingabe (der Inhalt von halb00.txt:)
15
1
4 5 10 1 6 4 0 7 6
2
3 -1.5 -6 0 -10 2 -6
5 -11 6 -13 -4 -7 -10 -3 -4 -3 2

In diesem Beispiel hat die Pizza den Radius 15. Es gibt einen Belag der ersten Sorte mit 4 Ecken. Gegen den Uhrzeigersinn aufgezählt sind die Koordinaten der Eckpunkte (5 | 10), (1 | 6), (4 | 0) und (7 | 6). Außerdem gibt es zwei Beläge der zweiten Sorte: einen mit den 3 Eckpunkten (–1.5 | –6), (0 | –10), (2 | –6) sowie einen mit den 5 Eckpunkten (–11 | 6), (–13 | –4), (–7 | –10), (–3 | –4), (–3 | 2).

Die Skizze (siehe Bild) zeigt, dass diese Pizza geteilt werden kann. Die Schnitt-Gerade hat den Winkel 310° (ein horizontaler Schnitt hätte den Winkel 0°). Ihre Geradengleichung lässt sich mit y = tan(310°)*x angeben. Auf jeder der beiden durch den Schnitt entstandenen Hälften liegen jeweils Beläge nur einer einzigen Sorte, wie gefordert. Dies kannst du überprüfen, indem du die x-Koordinate eines Eckpunktes in die Geradengleichung einsetzt und den errechneten Wert mit der y-Koordinate des Eckpunktes vergleichst.

Hier ist eine Blockly-Umgebung, mit der man diese Aufgabe bearbeiten kann.

Einlesedateien für die Arbeit mit Java folgen.