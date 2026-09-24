package JAVA1;

import java.util.Random;

public class test {
    public static void main(String[] args) {
        String gesuchtesWort = "Passw0rd!"; // Beispiel: das Wort, das gefunden werden soll
        Random rand = new Random();

        // Mögliches Zeichenset (Buchstaben, Zahlen, Sonderzeichen)
        String zeichenSet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#()-_=+:',.?";

        int minLaenge = 7;
        int maxLaenge = 30;

        int versuche = 0;
        boolean gefunden = false;

        while (!gefunden) {
            // Zufällige Länge zwischen min und max
            int laenge = rand.nextInt(maxLaenge - minLaenge + 1) + minLaenge;

            // Neue zufällige Zeichenkette bauen
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < laenge; i++) {
                char c = zeichenSet.charAt(rand.nextInt(zeichenSet.length()));
                sb.append(c);
            }
            String testWort = sb.toString();
            versuche++;

            // Prüfen, ob das generierte Wort dem gesuchten entspricht
            if (testWort.equals(gesuchtesWort)) {
                System.out.println("Wort gefunden nach " + versuche + " Versuchen: " + testWort);
                gefunden = true;
            }

            // Optional: Ausgabe aller 100000 Versuche
            if (versuche % 100000 == 0) {
                System.out.println("Versuch #" + versuche + ": " + testWort);
            }
        }
    }
}
