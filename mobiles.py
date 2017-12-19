###########
# Mobiles #
###########

def tree(root, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root] + list(branches)

def root(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def leaves(tree):
    if is_leaf(tree):
        return [root(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)], [])

def is_leaf(tree):
    return not branches(tree)

def mobile(left, right):
    """Construct a mobile from a left side and a right side."""
    return tree(None, [left, right])

def side(length, mobile_or_weight):
    """Construct a side: a length of rod with a mobile or weight at the end."""
    return tree(length, [mobile_or_weight])


def weight(size):
    """Construct a weight of some size."""
    assert size > 0
    "*** YOUR CODE HERE ***"
    return [size]

def sides(m):
    """Select the sides of a mobile."""
    return branches(m)

def length(s):
    """Select the length of a side."""
    return root(s)

def end(s):
    """Select the mobile or weight hanging at the end of a side."""
    return branches(s)[0]


def size(w):
    """Select the size of a weight."""
    "*** YOUR CODE HERE ***"
    return w[0]

def is_weight(w):
    """Whether w is a weight, not a mobile."""
    "*** YOUR CODE HERE ***"
    return w[1:] == []

def examples():
    t = mobile(side(1, weight(2)),
               side(2, weight(1)))
    u = mobile(side(5, weight(1)),
               side(1, mobile(side(2, weight(3)),
                              side(3, weight(2)))))
    v = mobile(side(4, t), side(2, u))
    return (t, u, v)


def total_weight(m):
    """Return the total weight of m, a weight or mobile.

    >>> t, u, v = examples()
    >>> total_weight(t)
    3
    >>> total_weight(u)
    6
    >>> total_weight(v)
    9
    """
    if is_weight(m):
        return size(m)
    else:
        return sum([total_weight(end(s)) for s in sides(m)])

def balanced(m):
    """Return whether m is balanced.

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> w = mobile(side(3, t), side(2, u))
    >>> balanced(w)
    False
    >>> balanced(mobile(side(1, v), side(1, w)))
    False
    >>> balanced(mobile(side(1, w), side(1, v)))
    False
    """
    "*** YOUR CODE HERE ***"
    l, r = sides(m)[0], sides(m)[1]
    l_len, r_len = l[0], r[0]
    l_wei_or_mob, r_wei_or_mob = l[1], r[1]
    if is_weight(l_wei_or_mob) and is_weight(r_wei_or_mob):             ##two weights
        return size(l_wei_or_mob) * l_len == size(r_wei_or_mob)*r_len
    elif is_weight(l_wei_or_mob) and not is_weight(r_wei_or_mob):       ##lweight rmobile
        return size(l_wei_or_mob) * l_len == total_weight(r_wei_or_mob)*r_len and balanced(r_wei_or_mob)
    elif not is_weight(l_wei_or_mob) and is_weight(r_wei_or_mob):       ##lmobile rweight
        return total_weight(l_wei_or_mob)*l_len == size(r_wei_or_mob)*r_len and balanced(l_wei_or_mob)
    elif not is_weight(l_wei_or_mob) and not is_weight(r_wei_or_mob):   ##two mobiles
        return total_weight(l_wei_or_mob)*l_len == total_weight(r_wei_or_mob)*r_len and balanced(l_wei_or_mob) and balanced(r_wei_or_mob)


def with_totals(m):
    """Return a mobile with total weights stored as the root of each mobile.

    >>> t, _, v = examples()
    >>> root(with_totals(t))
    3
    >>> print(root(t))                           # t should not change
    None
    >>> root(with_totals(v))
    9
    >>> [root(end(s)) for s in sides(with_totals(v))]
    [3, 6]
    >>> [root(end(s)) for s in sides(v)]         # v should not change
    [None, None]
    """
    "*** YOUR CODE HERE ***"
    l, r = sides(m)[0], sides(m)[1]
    l_len, r_len = l[0], r[0]
    l_wei_or_mob, r_wei_or_mob = l[1], r[1]
    wei = total_weight(l_wei_or_mob) + total_weight(r_wei_or_mob)
    if is_weight(l_wei_or_mob) and is_weight(r_wei_or_mob):             ##two weights
        return tree(wei, [l, r])
    elif is_weight(l_wei_or_mob) and not is_weight(r_wei_or_mob):       ##lweight rmobile
        return tree(wei, [l, [r_len, with_totals(r_wei_or_mob)]])
    elif not is_weight(l_wei_or_mob) and is_weight(r_wei_or_mob):       ##lmobile rweight
        return tree(wei, [[l_len, with_totals(l_wei_or_mob)], r])
    elif not is_weight(l_wei_or_mob) and not is_weight(r_wei_or_mob):   ##two mobiles
        return tree(wei, [[l_len, with_totals(l_wei_or_mob)], [r_len, with_totals(r_wei_or_mob)]])













