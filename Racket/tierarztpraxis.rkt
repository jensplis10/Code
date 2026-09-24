(define-record tier
make-tier
(tier-art arten)
(tier-name string)
(tier-geschlecht geschlecht)
(tier-alter natural)
(tier-gewicht real)
(tier-info string))

(define arten
(signature(enum "Hund" "Katze" "Kaninchen")))

(define geschlecht
(signature(enum "m" "w")))

(make-tier "Hund" "Snopy" "m" 15 19.2 "2 Stunden Auslauf")
(make-tier "Katze" "Seppel" "m" 7 4.4 "Freigänger")
(make-tier "Kaninchen" "Flocke" "w" 2 2.7 "")


(: get-tier-gewicht (tier -> real))
(define get-tier-gewicht
(lambda (t)
((tier-gewicht tier))))