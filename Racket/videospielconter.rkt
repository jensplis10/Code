#lang racket
(define conter 
(lambda (gegner)
(cond
((equal? gegner "Feuer") "Wasser")
((equal? gegner "Wasser") "Gras")
((equal? gegner "Gras") "Feuer")
(else "Kein Conter"))))

(conter "Feuer")
(conter "Wasser")
(conter "Gras")