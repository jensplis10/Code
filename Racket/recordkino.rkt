(define-record aufführungen
make-aufführung
(titel string)
(erste-vorstellung evorstellung)
(letzte-vorstellung lvorstellung)
(eintritt natural)
(fsk natural))

(define-record evorstellung
make-evorstellung
(e-tage natural)
(e-monat natural)
(e-jahr natural))

(define-record lvorstellung
make-lvorstellung
(l-tage natural)
(l-monat natural)
(l-jahr natural))

(define-record datum
make-datum
(tage natural)
(monat natural)
(jahr natural))

(define-record schueler
make-schueler
(schueler-name string)
(schueler-alter natural)
(schueler-gruppe boolean)
(schueler-testergebnis testergebnis))

(define-record testergebnis
make-testergebnis
(pretest natural)
(posttest natural))

(define läuft?
(lambda (a datum)
(if 
[equal? 
(and(<= (jahr datum) (l-jahr (letzte-vorstellung a)))
(and(>= (jahr datum) (e-jahr (erste-vorstellung a)))
(and(<= (monat datum) (l-monat (letzte-vorstellung a)))
(and(>= (monat datum) (e-monat (erste-vorstellung a)))
(and(<= (tage datum) (l-tage (letzte-vorstellung a)))
(>= (tage datum) (e-tage (erste-vorstellung a))))))))
 #t] "läuft" "läuft nicht")))

(define schueler-rabatt
(lambda (a s)
(if[>= (schueler-alter s) (fsk a)] (string-append "Der neue Preis beträgt " (number->string(* (eintritt a) 0.6))) (eintritt a))))

(läuft? (make-aufführung "Hallo" (make-evorstellung 12 12 2020) (make-lvorstellung 30 12 2020) 10 12)
 (make-datum 20 12 2021))

(schueler-rabatt (make-aufführung "Hallo" (make-evorstellung 12 12 2020) (make-lvorstellung 30 12 2020) 10 0)
 (make-schueler "Tan" 14 #t (make-testergebnis 44 76)))
