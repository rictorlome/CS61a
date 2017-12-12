##https://inst.eecs.berkeley.edu/~cs61a/fa16/hw/hw04/

import gmpy

from math import sqrt

def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    "*** YOUR CODE HERE ***"
    return [int(sqrt(x)) for x in s if gmpy.is_square(x) == 1]

"""
A mathematical function G on positive integers is defined by two cases:

G(n) = n,                                       if n <= 3
G(n) = G(n - 1) + 2 * G(n - 2) + 3 * G(n - 3),  if n > 3

"""
def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    else:
        return g(n-1) + 2 * g(n-2) + 3 * g(n-3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    else:
        three_back = 1
        two_back = 2
        one_back = 3
        i = 4
        while i <= n:
            cur = one_back + 2*two_back + 3*three_back
            three_back = two_back
            two_back = one_back
            one_back = cur
            i += 1
        return cur

"""
The ping-pong sequence counts up starting from 1 and is always either counting up or counting down.
At element k, the direction switches if k is a multiple of 7 or contains the digit 7.
The first 30 elements of the ping-pong sequence are listed below, with direction swaps marked using brackets at the 7th, 14th, 17th, 21st, 27th, and 28th elements:

1 2 3 4 5 6 [7] 6 5 4 3 2 1 [0] 1 2 [3] 2 1 0 [-1] 0 1 2 3 4 [5] [4] 5 6

Implement a function pingpong that returns the nth element of the ping-pong sequence. Do not use any assignment statements; however, you may use def statements.
"""
def has_seven(k):
    if k < 10:
        return k == 7
    else:
        return k%10 == 7 or has_seven(k//10)

def is_multiple_of_seven(k):
    return k % 7 == 0

def increment(k):
    return k + 1

def decrement(k):
    return k - 1

def increasing(n):
    return pingpong(n-1) > pingpong(n-2)

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif (increasing(n) and not (has_seven(n-1) or is_multiple_of_seven(n-1))) or (not increasing(n) and (has_seven(n-1) or is_multiple_of_seven(n-1))):
        return increment(pingpong(n-1))
    else:
        return decrement(pingpong(n-1))


"""
Once the machines take over, the denomination of every coin will be a power of two: 1-cent, 2-cent, 4-cent, 8-cent, 16-cent, etc. There will be no limit to how much a coin can be worth.

A set of coins makes change for n if the sum of the values of the coins is n. For example, the following sets make change for 7:

7 1-cent coins
5 1-cent, 1 2-cent coins
3 1-cent, 2 2-cent coins
3 1-cent, 1 4-cent coins
1 1-cent, 3 2-cent coins
1 1-cent, 1 2-cent, 1 4-cent coins

Thus, there are 6 ways to make change for 7. Write a function count_change that takes a positive integer n and returns the number of ways to make change for n using these coins of the future:
"""
def find_highest_coin(amount):
    i, coin = 1, 1
    while coin <= amount/2:
        coin = 2 ** i
        i += 1
    return coin

def is_power_of_two(num):
    quotient = num
    while quotient > 1:
        quotient /= 2
    return quotient == 1

def count_change(total):
    """Return the number of ways to make change for amount.
    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"
    highest_coin = find_highest_coin(total)
    avail_coins = [x for x in range(highest_coin+1) if is_power_of_two(x)]

    combinations = list(range(total+1))

    for i in range(total+1):
        combinations[i] = 0
    combinations[0] = 1

    for coin in avail_coins:
        for amount in range(total+1):
            if amount >= coin:
                combinations[amount] += combinations[amount-coin]

    return combinations[total]


