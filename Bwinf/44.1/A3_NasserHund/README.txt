Jede Datei enthält einen Plan eines Parks und ist so aufgebaut:

1. Zeile: Eine ganze Zahl k, die Anzahl der Wege im Park.
Folgende k Zeilen: Beschreibung je eines Weges definiert durch die x- und y-Koordinaten seiner Endpunkte.
In der nächsten Zeile: Eine ganze Zahl s, die Anzahl der Seen im Park.
Für jeden der s Seen folgen jeweils:
 Eine Zeile mit der Anzahl n seiner Eckpunkte.
 n Zeilen, die die Eckpunkte des Sees der Reihe nach beschreiben. Jede Zeile enthält die x- und y-Koordinate eines Eckpunkts. Die Eckpunkte der Seen werden immer in einer Reihenfolge (z.B. im Uhrzeigersinn) nacheinander angegeben.

Hier ist eine Beispieleingabe:

3
1 1 6 1
0 5 7 7
6 1 7 7
2
3
1 2
2 5
0 4
4
4 4
5 2
6 2
6 6

In diesem Beispiel gibt es im Park drei Wege. Die Strecke, die den ersten Weg beschreibt, hat den Startpunkt W1s=(1|1) und den Endpunkt W1e=(6|1). Die anderen beiden Wege werden analog durch die Stecken mit den Punkten W2s=(0|5), W2e=(7,7), W3s=(6|1), W3e=(7|7) beschrieben.
Außerdem gibt es im Park zwei Seen. Der erste See hat drei Eckpunkte: S11=(1|2), S12=(2|5) und S13=(0|4). Der zweite See hat vier Eckpunkte: S21=(4|4), S22=(5|2), S23=(6|2) und S24=(6|6).

Einlesedateien für die Arbeit mit Java werden Mitte September verfügbar sein.