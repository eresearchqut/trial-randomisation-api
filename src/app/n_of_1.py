'''n-of-1 functions'''
import string
import numpy as np


def randomise_schedule(number_of_patients: int, number_of_cycles: int, number_of_treatments: int):
    '''Randomise a n-of-1 schedule based on the number of patients, cycles and treatments in the trial'''
    return [__repeat_treatment(number_of_cycles, number_of_treatments) for _ in range(number_of_patients)]


def __repeat_treatment(number_of_cycles: int, number_of_treatments: int):
    return [__shuffle_treatment(number_of_treatments) for _ in range(number_of_cycles)]


def __shuffle_treatment(number_of_treatments: int):
    treatments = list(string.ascii_uppercase)[:number_of_treatments]
    np.random.default_rng().shuffle(treatments)
    return treatments
