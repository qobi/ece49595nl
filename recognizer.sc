(define (strip-a-word words lexicon)
 (if (null? words)
     (fail)
     (if (not (member (first words) lexicon))
	 (fail)
	 ;; word[1:]
	 (rest words))))

(define (strip-a-common-noun words)
 (strip-a-word words '(chair computer hat charger boat phone weed banana)))

(define (strip-a-proper-noun words)
 (strip-a-word words
	       '(Michael Richard-Nixon Taylor-Swift Donald-Trump Joe-Biden
			 Professor-Siskind JFK Mung-Chiang)))

(define (strip-a-determiner words)
 (strip-a-word words '(the a some every forty-two)))

;;; NP -> Nprop
;;;    |  DET Ncommon

(define (strip-a-noun-phrase words)
 (either (strip-a-proper-noun words)
	 (strip-a-common-noun (strip-a-determiner words))))

(define (strip-an-intransitive-verb words)
 (strip-a-word words '(ran died failed jumped cooked fell sang)))

(define (strip-a-transitive-verb words)
 (strip-a-word words '(ate smoked drank kissed fired)))

;;; VP -> Vintrans
;;;    |  Vtrans NP

(define (strip-a-verb-phrase words)
 (either (strip-an-intransitive-verb words)
	 (strip-a-noun-phrase (strip-a-transitive-verb words))))

;;; S -> NP VP

(define (strip-a-sentence words)
 (strip-a-verb-phrase (strip-a-noun-phrase words)))

(define (sentence? words)
 (not (not (member #t (all-values (null? (strip-a-sentence words)))))))
