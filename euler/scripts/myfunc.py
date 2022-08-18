
def fib(a, b):
    return a + b


def prime_factor(x):
    """ Return the prime factor of input x

    Parameters
    ----------
    x (int): input natural number > 1

    Return
    ------
    sorted_pf (set): list of prime factor of x """

    if not x:
        raise ValueError("Empty input.")

    if not isinstance(x, int):
        raise ValueError("Input value must be integer.")

    if x < 2:
        return None

    pf = set()
    while x > 1:
        for i in range(2, x + 1):
            if x % i == 0:
                x = int(x / i)
                pf.add(i)
                break
    sorted_pf = sorted(pf)

    return sorted_pf


def is_prime(n):
    """ Return whether the input n is prime number or not

    Parameters
    ----------
    n (int): input number

    Return
    ------
    result (bool): True if prime """

    if not isinstance(n, int) or n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def primes_below(n):
    """ Return prime numbers below n

    Parameters
    ----------
    n (int): Input value

    Return
    ------
    primes (list): List of prime numbers below n """

    if n <= 2:
        return []

    n = int(n)
    primes = [2]

    for i in range(3, n, 2):
        if is_prime(i):
            primes.append(i)

    return primes


def element_product(x):
    """ Return the product of all the element in list x

    Parameters
    ----------
    x (list): list of int numbers

    Return
    ------
    product (float): the greatest product of size n """

    if not x:
        return None

    if 0 in x:
        return 0

    product = 1
    for element in x:
        product *= element
    return product


def greatest_product(x, n):
    """ Return the greatest product of n consecutive numbers in list x

    Parameters
    ----------
    x (list): list of numbers
    n (int): size of consecurtive number

    Return
    ------
    greatest (float): the greatest product of size n """

    if len(x) < n:
        return None

    # the first product
    greatest = element_product(x[:n])

    # replace if greater
    for i in range(len(x) - n + 1):
        new = element_product(x[i:i + n])
        if new > greatest:
            greatest = new

    return greatest


def divisors(n):
    """ Return a list of divisors of positive int n

    Parameters
    ----------
    n (int): A number to be divided

    Return
    ------
    divisors (list of int): the divisors """

    if not isinstance(n, int) or n < 1:
        return []

    divisors = set([1, n])

    for i in range(2, int(n / 2)):
        if n % i == 0:
            divisors.add(i)
            divisors.add(int(n / i))

    return list(divisors)


def sign(n):
    """ Return sign 1 (n >= 0) or -1 (n < 0) """

    if not (isinstance(n, float) or isinstance(n, int)):
        raise ValueError("Input must be real number.")

    import math
    return math.copysign(1, n)


def num2lst(n):
    """ Convert from a multiple digit number to a list of single digit """
    return [int(i) if n > 0 else -int(i) for i in str(abs(n))]


def lst2num(lst):
    """ Convert from a list of single digits to a multiple digit number """

    # check all the element have the same sign
    if not all(sign(element) == sign(lst[0])
               for element in lst if element != 0):
        raise ValueError("All the element in lst must have the same sign.")

    num = int("".join([str(abs(i)) for i in lst]))
    return num if sign(lst[0]) > 0 else -num


def list_same_digit(n):
    """ Return the sorted list of the same digits from the input number

    Parameters
    ----------
    n (int): An int number

    Return
    ------
    digits (list of int): combination of digits """
    pass


def collatz_sequence(n):
    """ Return the list of Collatz sequences based on a rule:
    n → n/2 (n is even)
    n → 3n + 1 (n is odd)    
    
    Eg. collatz_sequence(13) returns
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
    
    Parameters
    ----------
    n (int): An int number

    Return
    ------
    seq (list of int): collatz_sequence """

    if not isinstance(n, int) or n < 1:
        return []
    
    seq = [n]
    
    while n > 1:
        if n%2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        seq.append(int(n))
    
    return seq

def longest_collatz_sequence(n):
    """ Return the longest Collatz sequence under n """
    
    if not isinstance(n, int) or n < 1:
        return 0    
    
    max_length = 0 # max length of seq
    max_n = 0 # the number that makes the longest seq 

    for i in range(1, n+1):
        seq = collatz_sequence(i)
        if len(seq) > max_length:
            max_length = len(seq)
            max_n = i
    
    return max_n