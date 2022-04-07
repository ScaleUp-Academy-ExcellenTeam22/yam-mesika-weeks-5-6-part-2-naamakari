# A perfect dish to share
from collections.abc import Generator


def perfect_number_dividing() -> Generator:
    """
    The function find all the perfect numbers.
    Perfect number is a number that equal to the sum of its divisors.
    :return: Generator, iterator that the callee function can pass over its elements
     even when it does not have them all.
    """
    # Start from 2 because every number divide by 1.
    divider = 2
    current_number = 2
    # Start from 1 because every number divide by 1, so it is part of the sum.
    divisors_sum = 1
    while True:
        while current_number > divider:
            if current_number % divider == 0:
                divisors_sum += divider
                divider += 1
            else:
                divider += 1
        if divisors_sum == current_number:
            yield current_number
            current_number += 1
            divider = 2
            divisors_sum = 1
        else:
            current_number += 1
            divider = 2
            divisors_sum = 1


if __name__ == '__main__':
    generator = perfect_number_dividing()
    while True:
        print(next(generator))

