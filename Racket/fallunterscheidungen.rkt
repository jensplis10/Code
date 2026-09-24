#lang racket
(define materialien #hash(("Holz" . 280)("Heu" . 260)("Getreide" . 250)("Holzkohle" . 300)("Zeitungspapier" . 175)))
;(: gefahr (String Integer -> Boolean))
(define gefahr 
(lambda (mat temp)
(if[< (hash-ref materialien mat) temp] "Gefahr" "Keine Gefahr")))

(gefahr "Heu" 3000)

