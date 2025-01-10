(define (a-common-noun)
 (either '(chair) '(computer) '(hat) '(charger) '(boat) '(phone) '(weed) '(banana)))

(define (a-proper-noun)
 (either '(Michael) '(Richard-Nixon) '(Taylor-Swift) '(Donald-Trump) '(Joe-Biden)
	 '(Professor-Siskind) '(JFK) '(Mung-Chiang)))

(define (a-determiner)
 (either '(the) '(a) '(some) '(every) '(forty-two)))

;;; NP -> Nprop
;;;    |  DET Ncommon

(define (a-noun-phrase)
 (either (a-proper-noun)
	 (append (a-determiner) (a-common-noun))))

(define (an-intransitive-verb)
 (either '(ran) '(died) '(failed) '(jumped) '(cooked) '(fell) '(sang)))

(define (a-transitive-verb)
 (either '(ate) '(smoked) '(drank) '(kissed) '(fired)))

;;; VP -> Vintrans
;;;    |  Vtrans NP

(define (a-verb-phrase)
 (either (an-intransitive-verb)
	 (append (a-transitive-verb) (a-noun-phrase))))

;;; S -> NP VP

(define (a-sentence)
 (append (a-noun-phrase) (a-verb-phrase)))

(define (slow-sentence? words)
 (not (not (member words (all-values (a-sentence))))))
