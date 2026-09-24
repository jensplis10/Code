;; Die ersten drei Zeilen dieser Datei wurden von DrRacket eingefügt. Sie enthalten Metadaten
;; über die Sprachebene dieser Datei in einer Form, die DrRacket verarbeiten kann.
#reader(lib "vanilla-reader.rkt" "deinprogramm" "sdp")((modname smartphone-betriebssysteme) (read-case-sensitive #f) (teachpacks ()) (deinprogramm-settings #(#f write repeating-decimal #f #t none explicit #f ())))
(define mar (signature(enum "Apple" "Google" "Huawei" "Samsung" "Sony" "Xiaomi")))
(define bet (signature(enum "iOS" "Android" "HarmonyOS" "Android" "Android" "Android")))
(: bs (mar -> bet))
(define bs
(lambda (marke)
(cond
((equal? marke "Apple") "iOS")
((equal? marke "Google") "Android")
(else "..."))))

(bs "Apple")
