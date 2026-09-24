(define-record punkt
make-punkt
(x-coord real)
(y-coord real))
(define achsen
(signature
(enum "x-Achse" "y-Achse" "keine Achse")))
(define abstand
(lambda (p1 p2)
(+ (if[>= (x-coord p1) (x-coord p2)] (- (x-coord p1) (x-coord p2)) (- (x-coord p2) (x-coord p1)))
(if[>= (y-coord p1) (y-coord p2)] (- (y-coord p1) (y-coord p2)) (- (y-coord p2) (y-coord p1))))))

(abstand (make-punkt 2 2) (make-punkt 1 1))



(define abstand-ursprung
(lambda (p)
(+ (if[>= (x-coord p) 0] (- (x-coord p) 0) (- 0 (x-coord p)))
(if[>= (y-coord p) 0] (- (y-coord p) 0) (- 0 (y-coord p))))))

(abstand-ursprung (make-punkt 0 0))


(: spiegeln (any achsen -> any))
(define spiegeln
(lambda (p achse)
(cond
([equal? achse "x-Achse"] (string-append (number->string(* (x-coord p) -1)) (string-append " " (number->string(y-coord p)))))
([equal? achse "y-Achse"] (string-append (string-append (number->string(x-coord p)) " ") (number->string(* (y-coord p) -1))))
(else p))))

(spiegeln (make-punkt 0 0) "x-Achse")