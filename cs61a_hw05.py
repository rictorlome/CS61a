## https://inst.eecs.berkeley.edu/~cs61a/fa16/hw/hw05/
## HW Begins on Line 5
##

def swap(a, b):
    """Swap the contents of lists a and b.

    >>> a = [1, 'two', 3]
    >>> b = [4, [5, 6]]
    >>> swap(a, b)
    >>> a
    [4, [5, 6]]
    >>> b
    [1, 'two', 3]
    """
    "*** YOUR CODE HERE ***"
    tmp = []
    len_a, len_b = len(a), len(b)
    for i in range(len_a):
        tmp += [a.pop(0)]
    for j in range(len_b):
        a += [b.pop(0)]
    len_tmp = len(tmp)
    for k in range(len_tmp):
        b += [tmp.pop(0)]

def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    other = 6 - (start + end)
    start_rod = [i for i in range(1,n+1)]
    other_rod = []
    end_rod = []
    move_counter = 1
    while move_counter == 1 or move_counter <= (n**2) - 1:
        if n % 2 == 0:
            if move_counter % 3 == 1:
                make_legal_move(start_rod, other_rod, start, other)
            elif move_counter % 3 == 2:
                make_legal_move(start_rod, end_rod, start, end)
            elif move_counter % 3 == 0:
                make_legal_move(other_rod, end_rod, other, end)
        elif n % 2 == 1:
            if move_counter % 3 == 1:
                make_legal_move(start_rod, end_rod, start, end)
            elif move_counter % 3 == 2:
                make_legal_move(start_rod, other_rod, start, other)
            elif move_counter % 3 == 0:
                make_legal_move(other_rod, end_rod, other, end)
        move_counter += 1

def make_legal_move(rod1_stack, rod2_stack, rod1, rod2):
    if rod1_stack == [] and rod2_stack == []:
        pass
    elif rod2_stack == []:
        rod2_stack.insert(0,rod1_stack.pop(0))
        print_move(rod1, rod2)
    elif rod1_stack == []:
        rod1_stack.insert(0,rod2_stack.pop(0))
        print_move(rod2, rod1)
    elif rod1_stack[0] < rod2_stack[0]:
        rod2_stack.insert(0,rod1_stack.pop(0))
        print_move(rod1, rod2)
    elif rod1_stack[0] > rod2_stack[0]:
        rod1_stack.insert(0,rod2_stack.pop(0))
        print_move(rod2, rod1)

def str_interval(x):
    """Return a string representation of interval x."""
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y."""
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

def interval(a, b):
    """Construct an interval from a to b."""
    return [a, b]

def lower_bound(x):
    """Return the lower bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[0]

def upper_bound(x):
    """Return the upper bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[1]

"""
Louis Reasoner has also provided an implementation of interval multiplication.
Beware: there are some data abstraction violations, so help him fix his code before someone sets it on fire.
"""
def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y."""
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return [min(p1, p2, p3, p4), max(p1, p2, p3, p4)]

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y."""
    "*** YOUR CODE HERE ***"
    return [lower_bound(x) - upper_bound(y), upper_bound(x) - lower_bound(y)]

def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided by
    any value in y. Division is implemented as the multiplication of x by the
    reciprocal of y."""
    "*** YOUR CODE HERE ***"
    assert upper_bound(y) != 0 and lower_bound(y) != 0, "Divide by zero?"
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)


def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))

def check_par():
    """Return two intervals that give different results for parallel resistors.

    >>> r1, r2 = check_par()
    >>> x = par1(r1, r2)
    >>> y = par2(r1, r2)
    >>> lower_bound(x) != lower_bound(y) or upper_bound(x) != upper_bound(y)
    True
    """
    r1 = interval(24, 100) # Replace this line!
    r2 = interval(24, 100) # Replace this line!
    return r1, r2

"""
Write a function quadratic that returns the interval of all values f(t) such that t is in the argument interval x and f(t) is a quadratic function:

f(t) = a*t*t + b*t + c
Make sure that your implementation returns the smallest such interval, one that does not suffer from the multiple references problem.

Hint: the derivative f'(t) = 2*a*t + b, and so the extreme point of the quadratic is -b/(2*a):
"""


def quadratic(x, a, b, c):
    """Return the interval that is the range of the quadratic defined by
    coefficients a, b, and c, for domain interval x.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    "*** YOUR CODE HERE ***"
    """
    NOT SURE.
    """


