def plus(x, y):
    return x+y

plus(3, 4)

def plus(u):
    x, y = u
    return x+y

plus((3, 4))

# Tupling

def plus((x, y)):
    return x+y

def pm(x, y):
    return x+y, x-y

u, v = pm(3, 4)

def pm(x, y):
    return (x+y, x-y)

(u, v) = pm(3, 4)

# ML, SML, OCaml

f(x, y, z)

f x

f (x, y)

def plus(x):
    def internal(y):
        return x+y
    return internal
plus(3)(4)

# Currying (Haskell Curry)

def plus x y:
    return x+y

((plus 3) 4)

# Haskell

a+b+c
((a+c)+c)

def f(x):
    return 2*x+1

two = 2
one = 1

def f(x):
    return two*x+one

# Lambda expressions
# Lambda calculus (Alonzo Church)

def plus(x):
    return lambda y: x+y

plus = lambda x: lambda y: x+y

S -> NP VP

typedef S = boolean

# NP(VP):S
# NP(VP):boolean

# NP:(alpha->S)(VP:alpha):S
# NP:(alpha->boolean)(VP:alpha):boolean

# typedef NP = alpha->S
# typedef VP = alpha

VP(NP)

sin(x)
n!

f:alpha->beta
x:alpha

(f x):beta

g:beta<-alpha
x:alpha

(x g):beta

 1. the type of a sentence is boolean
 2. the type of a noun is thing->boolean
 3. A N   --> A(N)
    D N   --> D(N)
    N PP  --> PP(N)
    NP VP --> VP(NP)
    P NP  --> P(NP)

primitive type boolean
primitive type thing
typedef N = thing->S    # thing->boolean
typedef A = N->N        # (thing->boolean)->(thing->boolean)
typedef D = N->NP       # (thing->boolean)->alpha
typedef P = NP->PP      # alpha->(N<-N)
typedef Vintrans = VP   # boolean<-alpha
typedef Vtrans = NP->VP # alpha->(S<-NP)
typedef NP = alpha
typedef VP = S<-NP      # boolean<-alpha
typedef S = boolean
typedef PP = N<-N       # (thing->boolean)<-(thing->boolean)

chair:thing->boolean
table:thing->boolean

big
red
round

big table
big chair
red table
red chair
round table
round chair

the table
the chair
some table
some chair
the big table
the big chair
some big table
some big chair

A(N):N
A:N->N

chair on the table
table on the table
table on the chair
chair on the chair

N PP

PP(N):N

PP:N<-N

the chair on the table
the table on the table
the table on the chair
the chair on the chair

the table
the chair

on the table
on the chair

on:P(the table:NP):PP
on:P(the chair:NP):PP

the
some
every

the chair
the table
some chair
some table
every chair
every table

the big chair
the big table
some big chair
some big table
every big chair
every big table

the chair on the table
the table on the table
some chair on the table
some table on the table
every chair on the table
every table on the table

D:N->NP(N):NP

lifted:NP->VP(some table:NP):VP
lifted some chair
lifted the table
lifted the chair
lifted every table
lifted every chair

all(lambda x:P(x))
some(lambda x:P(x))

all(lambda x:P(x), things)
some(lambda x:P(x), things)

all([...])
any([...])

all([P(x) for x in things])
any([P(x) for x in things])

--------------------------------------------------------------------------------------------------
typedef S = boolean
typedef N = thing->S
typedef D = N->NP
typedef VP = S<-NP
typedef NP = N->S

every:D = (lambda noun:
           (lambda noun1:
            (all(lambda x: noun(x)->noun1(x)))))

pawn:N = (lambda x: pawn(x))

moves:VP = (lambda subject_np:
            (subject_np(lambda x: moves(x))))

every:D(pawn:N):NP = (
    (lambda noun:
     (lambda noun1:
      (all(lambda x: noun(x)->noun1(x)))))
    (lambda x: pawn(x)))

every:D(pawn:N):NP = (
    (lambda noun:
     (lambda noun1:
      (all(lambda y: noun(y)->noun1(y)))))
    (lambda x: pawn(x)))

every:D(pawn:N):NP = (
    (lambda noun1:
     (all(lambda y: ((lambda x: pawn(x))(y))->noun1(y)))))

every:D(pawn:N):NP = (
    (lambda noun1: (all(lambda y: pawn(y)->noun1(y)))))

# Every pawn moves
moves:VP(every:D(pawn:N):NP):S = (
    (lambda subject_np:
     (subject_np(lambda x: moves(x))))
    (lambda noun1: (all(lambda y: pawn(y)->noun1(y)))))

moves:VP(every:D(pawn:N):NP):S = (
    ((lambda noun1: (all(lambda y: pawn(y)->noun1(y))))
     (lambda x: moves(x))))

moves:VP(every:D(pawn:N):NP):S = (
    (all(lambda y: pawn(y)->((lambda x: moves(x))(y)))))

# Every pawn moves
moves:VP(every:D(pawn:N):NP):S = (all(lambda y: pawn(y)->moves(y)))

every = (lambda noun:
         (lambda noun1:
          (all([noun(x)->noun1(x) for x in things]))))

pawn = (lambda x: pawn(x))

moves = (lambda subject_np: (subject_np(lambda x: moves(x))))

moves(every(pawn)) = all([pawn(y)->moves(y) for y in things])
