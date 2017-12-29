## Link class and class methods taken from Composing Programs Section 2.9.1
## http://composingprograms.com/pages/29-recursive-objects.html


class Link:
    """A linked list with a first element and the rest."""
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]
    def __len__(self):
        return 1 + len(self.rest)


def link_expression(s):
        """Return a string that would evaluate to s."""
        if s.rest is Link.empty:
            rest = ''
        else:
            rest = ', ' + link_expression(s.rest)
        return 'Link({0}{1})'.format(s.first, rest)

Link.__repr__ = link_expression

def digits(n):
    """Return the digits of n as a linked list.

    >>> digits(0) is Link.empty
    True
    >>> digits(543)
    Link(5, Link(4, Link(3)))
    """
    s = Link.empty
    while n > 0:
        n, last = n // 10, n % 10
        "*** YOUR CODE HERE ***"
        s = Link(last, s)
    return s

class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    """

    def __init__(self):
        self.value = 0

    def next(self):
        "*** YOUR CODE HERE ***"
        cur = Fib()
        if self.value is 0:
            cur.value = 1
        else:
            cur.value = self.value + self.prev
        cur.prev = self.value
        return cur

    def __repr__(self):
        return str(self.value)



class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, prod, cost):
        self.prod = prod
        self.cost = cost
        self.stock = 0
        self.balance = 0

    def vend(self):
        if self.stock is 0:
            return 'Machine is out of stock.'
        elif self.balance < self.cost:
            return 'You must deposit ${0} more.'.format(self.cost-self.balance)
        else:
            change = self.balance - self.cost
            self.balance = 0
            self.stock -= 1
            if change is 0:
                return 'Here is your {0}.'.format(self.prod)
            else:
                return 'Here is your {0} and ${1} change.'.format(self.prod, change)

    def restock(self, num):
        self.stock += num
        return 'Current {0} stock: {1}'.format(self.prod, self.stock)

    def deposit(self, amt):
        if self.stock is 0:
            return 'Machine is out of stock. Here is your ${0}.'.format(amt)
        else:
            self.balance += amt
            return 'Current balance: ${0}'.format(self.balance)


class MissManners:
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'

    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon.'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'

    >>> double_fussy = MissManners(m) # Composed MissManners objects
    >>> double_fussy.ask('deposit', 10)
    'You must learn to say please first.'
    >>> double_fussy.ask('please deposit', 10)
    'Thanks for asking, but I know not how to deposit.'
    >>> double_fussy.ask('please please deposit', 10)
    'Thanks for asking, but I know not how to please deposit.'
    >>> double_fussy.ask('please ask', 'please deposit', 10)
    'Current balance: $10'
    """
    def __init__(self, obj):
        self.obj = obj

    def ask(self, message, *args):
        magic_word = 'please '
        leng = len(magic_word)
        if not message.startswith(magic_word):
            return 'You must learn to say please first.'
        else:
            if hasattr(self.obj, message[leng:]):
                x = getattr(self.obj, message[leng:])
                if x.__code__.co_argcount == len(args)+1:       #I think this +1 is because self is an argument for these funcs. The ifs in lines 192-195 make the doctest fail, bc arg count is wrong. It works without them.
                    return x(*args)
                else:
                    return 'Thanks for asking, but you must learn to count your args.'
            else:
                return 'Thanks for asking, but I know not how to {0}.'.format(message[leng:])
