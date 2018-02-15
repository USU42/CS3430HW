#!/usr/bin/python

#########################################
## CS 3430: S2018: HW01: Euclid Numbers
## Kelsye Anderson
## A02093326
#########################################

import math

def is_prime(n):
    '''is_prime(n) ---> True if n is prime; False otherwise.'''
    # your code here
    ans = True

    for x in xrange(2,(n-1)):
        if ((n%x) == 0):
            ans = False

    if n == 0 or n == 1:
        ans = False

    return ans

def next_prime_after(p):
    '''computes next prime after prime p; if p is not prime, returns None.'''
    if not is_prime(p): return None
    ## your code here
    found = False
    x = p
    while not found:
        x += 1
        found = is_prime(x)

    return x

def euclid_number(i):
    '''euclid_number(i) --> i-th Euclid number.'''
    if i < 0: return None
   ## your code here
    prime = 3
    ans = 2
    count = 0
    if i == 0:
        ans = 3
        return ans
    while count != i:
        count += 1
        ans *= prime
        prime = next_prime_after(prime)

    return ans+1

def compute_first_n_eucs(n):
    '''returns a list of the first n euclid numbers.'''
    eucs = []
    ## your code here
    for x in xrange(0,n):
        eucs.append(euclid_number(x))

    return eucs

def prime_factors_of(n):
    '''returns a list of prime factors of n if n > 1 and [] otherwise.'''
    if n < 2: return []
    factors = []
    ## your code here
    num = n
    if is_prime(n): return n
    while num != 1:
        prime = 2
        while (num % prime) != 0:
            prime = next_prime_after(prime)
        factors.append(prime)
        num /= prime

    return factors

def tabulate_euc_factors(n):
    '''returns a list of 3-tuples (i, euc, factors).'''
    euc_factors = []
    ## your code here

    for x in xrange(0,n + 1):
        euc_factors.append((x, euclid_number(x), prime_factors_of(euclid_number(x))))

    return euc_factors

def pair(x, y):
    '''returns z such that <x, y> = z.'''
    ## your code
    ans = pow(2,x)*((2*y) + 1) - 1
    return ans

def find_pair_of(z):
    '''returns the tuple (x, y) such that <x, y> = z.'''
    ## your code
    num = pow(2,0)
    count = -1
    x = 0
    while num < (z + 1):
        count += 1
        num = pow(2, count)
        if (z+1) % num == 0:
            x = count

    y = 0
    f = (2*y)+ 1
    while f != (z+1)/pow(2,x):
        y += 1
        f = (2 * y) + 1

    return (x,y)

def left_of(z):
    '''returns x such that <x, y> = z.'''
    ## your code
    x = find_pair_of(z)[0]
    return 0

def right_of(z):
    '''returns y such that <x, y> = z.'''
    ## your code
    y = find_pair_of(z)[1]
    return y



