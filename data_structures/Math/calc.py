from math import exp, erf, sqrt, expm1

print((1e-5) - 1)

def phi(x):
    'Cumulative distribution function for the standard normal distribution'
    return (1.0 + erf(x / sqrt(2.0))) / 2.0

print(phi(39))

