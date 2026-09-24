package JAVA1;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Neu {

    static String gesuchtesWort = "Passw0rd";
    static String zeichenSet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    static volatile boolean gefunden = false;
    static long versuche = 0;
    static int minLaenge = 8;
    static int maxLaenge = 8; // Eingrenzen, falls bekannt

    public static void main(String[] args) {
        int threadAnzahl = Runtime.getRuntime().availableProcessors(); // z. B. 8
        ExecutorService executor = Executors.newFixedThreadPool(threadAnzahl);

        for (int laenge = minLaenge; laenge <= maxLaenge; laenge++) {
            System.out.println("Starte Threads für Länge: " + laenge);

            for (int i = 0; i < zeichenSet.length(); i++) {
                final char startChar = zeichenSet.charAt(i);
                final int zielLaenge = laenge;

                executor.submit(() -> {
                    char[] current = new char[zielLaenge];
                    current[0] = startChar;
                    backtrack(current, 1, zielLaenge);
                });
            }
        }

        executor.shutdown(); // Kein neuer Task mehr

        // Warten bis alle Threads fertig
        while (!executor.isTerminated()) {
            if (gefunden)
                break;
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        if (!gefunden) {
            System.out.println("Wort nicht gefunden.");
        }
    }

    static synchronized void incrementVersuche() {
        versuche++;
    }

    static void backtrack(char[] current, int pos, int laenge) {
        if (gefunden)
            return;

        if (pos == laenge) {
            incrementVersuche();
            String testWort = new String(current);
            if (testWort.equals(gesuchtesWort)) {
                System.out.println("✅ Wort gefunden nach " + versuche + " Versuchen: " + testWort);
                gefunden = true;
            }
            if (versuche % 1_000_000 == 0) {
                System.out.println("Versuch #" + versuche + ": " + testWort);
            }
            return;
        }

        for (int i = 0; i < zeichenSet.length(); i++) {
            if (gefunden)
                return;
            current[pos] = zeichenSet.charAt(i);
            backtrack(current, pos + 1, laenge);
        }
    }
}
