##CS61a 2016 - Lab 3
##https://inst.eecs.berkeley.edu/~cs61a/fa16/lab/lab03

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    print(n)
    counter = 1
    if n == 1:
        return counter
    if n % 2 == 0:
        counter += hailstone(n//2)
    if n % 2 == 1:
        counter += hailstone(n*3+1)
    return counter


def ab_plus_c(a, b, c):
    """Computes a * b + c.

    >>> ab_plus_c(2, 4, 3)  # 2 * 4 + 3
    11
    >>> ab_plus_c(0, 3, 2)  # 0 * 3 + 2
    2
    >>> ab_plus_c(3, 0, 2)  # 3 * 0 + 2
    2
    """
    "*** YOUR CODE HERE ***"
    if a == 0 or b == 0:
        return c
    if a == 1:
        return b + c
    if b == 1:
        return a + c
    else:
        return ab_plus_c(a-1, b, c) + b

def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    """
    For reference:

        x, y = n, 0
    f = lambda: _____
    while x > 0:
        x, y = _____, f()
    return y == n
    """
    x, y = n, 0
    f = lambda: 10 * y + x % 10
    while x > 0:
        x, y = x//10, f()
    return y == n
