(define-structure state stack words)

(define (parse-a-word state category lexicon)
 (let ((stack (state-stack state))
       (words (state-words state)))
  (if (null? words)
      (fail)
      (if (not (member (first words) lexicon))
	  (fail)
	  (make-state
	   (cons (list category (first words)) stack)
	   (rest words))))))

(define (pop-one category state)
 (let ((stack (state-stack state))
       (words (state-words state)))
  (make-state (cons (list category (first stack)) (rest stack))
	      words)))


(define (pop-two category state)
 (let ((stack (state-stack state))
       (words (state-words state)))
  (make-state (cons (list category (second stack) (first stack))
		    (rest (rest stack)))
	      words)))

(define (parse-a-common-noun state)
 (parse-a-word
  state 'n-common '(cat chair blueberry ice-cream dumpster computer weed hair)))

(define (parse-a-proper-noun state)
 (parse-a-word
  state
  'n-proper
  '(Japan Purdue Chipotle Yosemite Donald-Trump Mung-Chiang Elon-Musk
	  Bradon-Smith Taylor-Swift)))

(define (parse-a-determiner state)
 (parse-a-word state 'det '(the a some every forty-two)))

;;; NP -> Nprop
;;;    | DET Ncommon

(define (parse-a-noun-phrase state)
 (either (pop-one 'np (parse-a-proper-noun state))
	 (pop-two 'np (parse-a-common-noun (parse-a-determiner state)))))

(define (parse-an-intransitive-verb  state)
 (parse-a-word
  state
  'v-intrans
  '(ran spoke ate swam juggled failed passed vomited slept screwed-up)))

(define (parse-a-transitive-verb state)
 (parse-a-word
  state 'v-trans '(pushed pulled slapped kissed smoked fought fired)))

;;; VP -> Vintrans
;;;    |  Vtrans NP

(define (parse-a-verb-phrase state)
 (either (pop-one 'vp (parse-an-intransitive-verb state))
	 (pop-two 'vp (parse-a-noun-phrase (parse-a-transitive-verb state)))))

;;; S -> NP VP

(define (parse-a-sentence state)
 (pop-two 's (parse-a-verb-phrase (parse-a-noun-phrase state))))

(define (a-parse words)
 (let* ((state (parse-a-sentence (make-state '() words)))
	(stack (state-stack state))
	(words (state-words state)))
  (if (and (null? words)
	   (= (length stack) 1)
	   (eq? (first (first stack)) 's))
      (first stack)
      (fail))))
