#!/usr/bin/env python


import math
import copy
import itertools


def get_maximums(numbers: list[list[int]]) -> list[int]:
    return [max(n) for n in numbers]


def join_integers(numbers: list[int]) -> int:
    return int("".join([str(n) for n in numbers]))


def generate_prime_numbers(limit: int):
    premiers = []
    nombres = [i for i in range(2, limit + 1)]
    while nombres:
        premiers.append(nombres[0])
        nombres = [n for n in nombres if n % nombres[0] != 0]

    return premiers


def combine_strings_and_numbers(
    strings: list[str],
    num_combinations: int,
    excluded_multiples: int | None,
) -> list[str]:
    resultat = []

    for i in range(1, num_combinations + 1):
        if excluded_multiples and i % excluded_multiples == 0:
            continue
        else:
            resultat.extend([s + str(i) for s in strings])

    return resultat


if __name__ == "__main__":
    print(get_maximums([[1, 2, 3], [6, 5, 4], [10, 11, 12], [8, 9, 7]]))
    print("")
    print(join_integers([111, 222, 333]))
    print(join_integers([69, 420]))
    print("")
    print(generate_prime_numbers(17))
    print("")
    print(combine_strings_and_numbers(["A", "B"], 2, None))
    print(combine_strings_and_numbers(["A", "B"], 5, 2))
