#lang racket
(define binär-zu-farbe
(lambda (code)
(cond
([equal? code "001"] "blau")
([equal? code "010"] "grün")
([equal? code "100"] "rot")
([equal? code "110"] "gelb")
(else "Uneindeutig"))))

(binär-zu-farbe "100")


(define pH-Wert-MR
(lambda (farbe)
(cond
([string=? "rot" farbe] "pH <= 5.1")
([string=? "gelb" farbe] "pH-Wert > 5.1")
(else "unbekannte Farbe"))))

(pH-Wert-MR "rot")
(pH-Wert-MR "gelb")


(pH-Wert-MR(binär-zu-farbe "110"))

;(define pH-Indikator-Farbe
;(signature (enum "blau" "grün" "rot" "gelb" "uneindeutig")))