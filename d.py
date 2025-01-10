every = (
    lambda noun: (
        lambda noun1: (
            every(lambda x: noun(x)->noun1(x)))))

some = (
    lambda noun: (
        lambda noun1: (
            some(lambda x: noun(x) and noun1(x)))))

pawn = (lambda x: pawn(x))

square = (lambda x: square(x))

is_on1 = (
    lambda object_np: (
        lambda subject_np: (
            subject_np(lambda x: object_np(lambda y: on(x, y))))))

is_on2 = (
    lambda object_np: (
        lambda subject_np: (
            object_np(lambda y: subject_np(lambda x: on(x, y))))))

# Every pawn is on some square
# Every pawn is_on some square

every(pawn) = (
    (lambda noun: (
        lambda noun1: (
            every(lambda x: noun(x)->noun1(x)))))
    (lambda x: pawn(x)))

every(pawn) = (
    (lambda noun: (
        lambda noun1: (
            every(lambda x: noun(x)->noun1(x)))))
    (lambda y: pawn(y)))

every(pawn) = (
    lambda noun1: (
        every(lambda x: ((lambda y: pawn(y))
                         (x))->noun1(x))))

every(pawn) = (
    lambda noun1: (
        every(lambda x: pawn(x))->noun1(x)))

some(square) = (
    (lambda noun: (
        lambda noun1: (
            some(lambda x: noun(x) and noun1(x)))))
    (lambda x: square(x)))

some(square) = (
    (lambda noun: (
        lambda noun1: (
            some(lambda x: noun(x) and noun1(x)))))
    (lambda y: square(y)))

some(square) = (
    lambda noun1: (
        some(lambda x: ((lambda y: square(y))
                        (x)) and noun1(x))))

every(pawn) = (
    lambda noun1: (
        every(lambda x: pawn(x))->noun1(x)))

some(square) = (
    lambda noun1: (
        some(lambda x: square(x) and noun1(x))))

is_on1 = (
    lambda object_np: (
        lambda subject_np: (
            subject_np(lambda x: object_np(lambda y: on(x, y))))))

is_on1(some(square)) = (
    (lambda object_np: (
        lambda subject_np: (
            subject_np(lambda x: object_np(lambda y: on(x, y))))))
    (lambda noun1: (
        some(lambda x: square(x) and noun1(x)))))

is_on1(some(square)) = (
    (lambda object_np: (
        lambda subject_np: (
            subject_np(lambda x: object_np(lambda y: on(x, y))))))
    (lambda noun1: (
        some(lambda w: square(w) and noun1(w)))))

is_on1(some(square)) = (
    lambda subject_np: (
        subject_np(lambda x: ((lambda noun1: (
            some(lambda w: square(w) and noun1(w))))
                              (lambda y: on(x, y))))))

is_on1(some(square)) = (
    lambda subject_np: (
        subject_np(lambda x: (
            some(lambda w: square(w) and ((lambda y: on(x, y))
                                          (w)))))))

is_on1(some(square)) = (
    lambda subject_np: (
        subject_np(lambda x: (
            some(lambda w: square(w) and on(x, w))))))

is_on1(some(square))(every(pawn)) = (
    (lambda subject_np: (
        subject_np(lambda x: (
            some(lambda w: square(w) and on(x, w))))))
    (lambda noun1: (
        every(lambda x: pawn(x))->noun1(x))))

is_on1(some(square))(every(pawn)) = (
    (lambda subject_np: (
        subject_np(lambda x: (
            some(lambda w: square(w) and on(x, w))))))
    (lambda noun1: (
        every(lambda z: pawn(z))->noun1(z))))

is_on1(some(square))(every(pawn)) = (
    ((lambda noun1: (
        every(lambda z: pawn(z))->noun1(z)))
     (lambda x: (
         some(lambda w: square(w) and on(x, w))))))

is_on1(some(square))(every(pawn)) = (
        every(lambda z: pawn(z))->((lambda x: (
         some(lambda w: square(w) and on(x, w))))
                                   (z)))

# Every pawn is_on1 some square
is_on1(some(square))(every(pawn)) = (
        every(lambda z: pawn(z)->(some(lambda w: square(w) and on(z, w)))))

is_on2(some(square)) = (
    (lambda object_np: (
        lambda subject_np: (
            object_np(lambda y: subject_np(lambda x: on(x, y))))))
    (lambda noun1: (
        some(lambda x: square(x) and noun1(x)))))

is_on2(some(square)) = (
    (lambda object_np: (
        lambda subject_np: (
            object_np(lambda y: subject_np(lambda x: on(x, y))))))
    (lambda noun1: (
        some(lambda w: square(w) and noun1(w)))))

is_on2(some(square)) = (
    lambda subject_np: (
        ((lambda noun1: (
            some(lambda w: square(w) and noun1(w))))
         (lambda y: subject_np(lambda x: on(x, y))))))

is_on2(some(square)) = (
    lambda subject_np: (
        some(lambda w: square(w) and ((lambda y: subject_np(lambda x: on(x, y)))
                                      (w)))))

is_on2(some(square)) = (
    lambda subject_np: (
        some(lambda w: square(w) and subject_np(lambda x: on(x, w)))))

is_on2(some(square))(every(pawn)) = (
    (lambda subject_np: (
        some(lambda w: square(w) and subject_np(lambda x: on(x, w)))))
    (lambda noun1: (
            every(lambda x: pawn(x))->noun1(x))))

is_on2(some(square))(every(pawn)) = (
    (lambda subject_np: (
        some(lambda w: square(w) and subject_np(lambda x: on(x, w)))))
    (lambda noun1: (
            every(lambda z: pawn(z))->noun1(z))))

is_on2(some(square))(every(pawn)) = (
    some(lambda w: square(w) and ((lambda noun1: (
        every(lambda z: pawn(z))->noun1(z)))
                                  (lambda x: on(x, w)))))

is_on2(some(square))(every(pawn)) = (
    some(lambda w: square(w) and (
        every(lambda z: pawn(z))->((lambda x: on(x, w))
                                   (z)))))

is_on2(some(square))(every(pawn)) = (
    some(lambda w: square(w) and (every(lambda z: pawn(z))->on(z, w))))
