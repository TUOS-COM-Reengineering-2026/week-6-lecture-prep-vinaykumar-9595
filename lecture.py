# PART 1
def is_palindrome(s):
    # Iterative solution to avoid RecursionError
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


# PART 2
def is_small(a):
    # Simplified version
    return a < 5


def randomised_function(a=None):
    from random import randint

    # Allow controlled input for testing
    if a is None:
        a = randint(0, 10)

    if is_small(a):
        return 'software'
    else:
        return 'engineering'


# PART 3 (Advanced Topic)
def difficult_function(x, y):
    if complex_math(x, y) < 0.000001:
        return 'solved!'
    else:
        return 'not yet'


def complex_math(x, y):
    import numpy as np
    a = 20
    b = 0.2
    c = 2 * np.pi

    t1 = -a * np.exp(-b * np.sqrt(0.5 * ((x - 10) ** 2 + y ** 2)))
    t2 = -np.exp(0.5 * (np.cos(c * (x - 10)) + np.cos(c * y)))

    return t1 + t2 + a + np.e


# MAIN (Testing)
if __name__ == '__main__':
    # PART 1 tests
    print(is_palindrome("madam"))     # True
    print(is_palindrome("hello"))     # False
    print(is_palindrome("a" * 10000)) # No RecursionError

    # PART 2 tests
    print(randomised_function(2))     # software
    print(randomised_function(7))     # engineering
    print(randomised_function())      # random

    # PART 3 test (coverage)
    print(difficult_function(10, 0))  # solved!
