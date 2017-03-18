import math

def has_complete_sequence(a,m,c):
    return coprime(m,c) and divisible_by_factors(a,m) and four_divides(m,a)

def coprime(a,b):
    return math.gcd(a,b) == 1

def prime_factors(m):
    prime_factors = []
    d = 2
    while d*d <= m:
        while (m % d) == 0:
            if d not in prime_factors:
                prime_factors.append(d)
            m //= d
        d += 1
    if m > 1:
        prime_factors.append(m)
    return prime_factors

def divisible_by_factors(a,m):
    primes = prime_factors(m)
    a = a-1
    for p in primes:
        """
        Si no lo divide alguno de los
        factores primos, return False
        """
        if a%p !=0:
            return False
    return True

def four_divides(m,a):
    a = a-1
    return m%4 == 0 and a%4 == 0;
