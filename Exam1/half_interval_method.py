#!/usr/bin/python3

#########################################
## module: half_interval_method.py
# Kelsye Anderson
# A02093326
#########################################

from __future__  import  division
import math


def close_enough(x, y, error = 0.00000000000001):
    return abs(x - y) < error


def find_midpoint(f, neg_point, pos_point):
    # your code
    x = (neg_point + pos_point) / 2
    if close_enough(neg_point, pos_point):
        return x
    else:
        if f(x) is 0:
            return f
        elif f(x) > 0:
            return half_interval_method(f, neg_point, x)
        elif f(x) < 0:
            return half_interval_method(f, x, pos_point)


def half_interval_method(f, a, b):
    a_val = f(a)
    b_val = f(b)
    if a_val < 0 and b_val > 0:
        return find_midpoint(f, a, b)
    elif b_val < 0 and a_val > 0:
        return find_midpoint(f, b, a)
    else:
        raise Exception('Values are not of opposite sign')


# print("Test 1")
# print(math.sin(2.0))
# print(math.sin(4.0))
# x = half_interval_method(math.sin, 2.0, 4.0)
# print(x)
# print(math.sin(x))
# print("-------------------------")
#
# print("Test 2")
# x = half_interval_method(math.cos, 0, 2)
# print(x)
# print(math.cos(x))
# print("-------------------------")
#
# print("Test 3")
# x = half_interval_method(lambda x: 20*x**3 - 10*x**2 - 5*x - 1, 0, 1)
# print(x)
# print((lambda x: 20*x**3 - 10*x**2 - 5*x - 1)(x))
# print("-------------------------")
#
