def make_counter():
    """Return a counter function.

    >>> c = make_counter()
    >>> c('a')
    1
    >>> c('a')
    2
    >>> c('b')
    1
    >>> c('a')
    3
    >>> c2 = make_counter()
    >>> c2('b')
    1
    >>> c2('b')
    2
    >>> c('b') + c2('b')
    5
    """
    "*** YOUR CODE HERE ***"
    str_count = {}
    def counter(str):
        nonlocal str_count
        if str not in str_count:
            str_count[str] = 1
        else:
            str_count[str] += 1
        return str_count[str]
    return counter

def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    """
    "*** YOUR CODE HERE ***"
    count = 0
    last_fib = 1
    scnd_last_fib = 0
    def next_fib():
        nonlocal count
        nonlocal last_fib
        nonlocal scnd_last_fib
        count += 1
        if count == 1:
            return 0
        elif count == 2:
            return 1
        else:
            nxt_fib = last_fib + scnd_last_fib
            scnd_last_fib = last_fib
            last_fib = nxt_fib
            return last_fib
    return next_fib

class Account:
    """An account has a balance and a holder.

    >>> a = Account('John')
    >>> a.deposit(10)
    10
    >>> a.balance
    10
    >>> a.interest
    0.02

    >>> a.time_to_retire(10.25) # 10 -> 10.2 -> 10.404
    2
    >>> a.balance               # balance should not change
    10
    >>> a.time_to_retire(11)    # 10 -> 10.2 -> ... -> 11.040808032
    5
    >>> a.time_to_retire(100)
    117
    """

    interest = 0.02  # A class attribute

    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        """Add amount to balance."""
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Subtract amount from balance if funds are available."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

    def time_to_retire(self, amount):
        """Return the number of years until balance would grow to amount."""
        assert self.balance > 0 and amount > 0 and self.interest > 0
        "*** YOUR CODE HERE ***"
        year = 0
        track_balance = self.balance
        while track_balance < amount:    
            year += 1
            track_balance = track_balance*(1+self.interest)
        return year    

class FreeChecking(Account):
    """A bank account that charges for withdrawals, but the first two are free!

    >>> ch = FreeChecking('Jack')
    >>> ch.balance = 20
    >>> ch.withdraw(3)    # First one's free
    17
    >>> ch.withdraw(100)  # And the second
    'Insufficient funds'
    >>> ch.balance
    17
    >>> ch.withdraw(3)    # Ok, two free withdrawals is enough
    13
    >>> ch.withdraw(3)
    9
    >>> ch2 = FreeChecking('John')
    >>> ch2.balance = 10
    >>> ch2.withdraw(3) # No fee
    7
    >>> ch.withdraw(3)  # ch still charges a fee
    5
    """
    withdraw_fee = 1
    free_withdrawals = 2
    "*** YOUR CODE HERE ***"
    
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0
        self.free_withdrawals_left = self.free_withdrawals
        
    def withdraw(self, amount):
        """Subtract amount from balance if funds are available."""
        self.free_withdrawals_left -= 1
        if amount > self.balance:
            return 'Insufficient funds'
        elif self.free_withdrawals_left >= 0:
            self.balance = self.balance - amount
        else:
            self.balance = self.balance - amount - self.withdraw_fee
        return self.balance

