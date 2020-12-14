"""n-of-1 functions"""
import string
import itertools
import numpy as np
from aws_xray_sdk.core import xray_recorder


@xray_recorder.capture()
def randomise_n_of_1_schedule(number_of_patients: int, number_of_cycles: int, number_of_treatments: int):
    """Randomise a n-of-1 schedule based on the number of patients, cycles and treatments in the trial"""
    schedules = itertools.chain.from_iterable(shuffled_block(number_of_cycles, number_of_treatments))
    return list(itertools.islice(schedules, number_of_patients))


def shuffled_block(number_of_cycles: int, number_of_treatments: int):
    b = list(block(number_of_cycles, number_of_treatments))

    while True:
        np.random.default_rng().shuffle(b)
        yield b


def block(number_of_cycles: int, number_of_treatments: int):
    permutations = permutate(number_of_treatments)
    return itertools.product(permutations, repeat=number_of_cycles)


def permutate(number_of_treatments: int):
    treatments = string.ascii_uppercase[:number_of_treatments]
    return itertools.permutations(treatments)
