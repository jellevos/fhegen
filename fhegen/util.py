import math
from sympy import n_order, nextprime, totient


def clog2(x):
    return int(math.ceil(math.log2(x)))


def phi(x) -> int:
    ans = totient(x)
    return ans  # type: ignore


def estsecurity(m, logq, sdist):
    d = phi(m)

    if sdist == 'Ternary':
        alpha = 0.05
        beta = 0.33
        gamma = 17.88
        delta = 0.65
    elif sdist == 'Error':
        alpha = 3.87
        beta = 0.74
        gamma = 12.72
        delta = 0.17

    est = -math.log2(alpha * logq / d) * beta * d / logq + gamma * pow(logq / d, delta) * math.log2(d / logq)
    return max(int(math.floor(est)), 0)


def genprime(start, m=0, batch=False):
    p = nextprime(start - 1)

    if batch:
        while p % m != 1:  # type: ignore
            p = nextprime(p)

    return p


def gent(m, gen, t, logt, batch):
    if gent:
        return genprime(2**(logt - 1), m, batch)
    else:
        return t


def slots(m, t):
    return phi(m) / n_order(t, m)
