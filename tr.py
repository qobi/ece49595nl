def f(x):
    return ...

def g(x):
    return ...

def h(x):
    return g(f(x))

old_f = f
old_g = g

def new_f(x):
    if tuple(x):
        return (old_f(x[0]), (times_df_dx, x))
    else:
        return old_f(x)

def new_g(x):
    if tuple(x):
        return (old_g(x[0]), (times_dg_dx, x))
    else:
        return old_g(x)

f = new_f
g = new_g

def variable(x):
    return (x, "x")

h(5)
h(variable(5))
(h(5), ...)
