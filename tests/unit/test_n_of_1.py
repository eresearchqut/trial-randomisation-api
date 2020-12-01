import pytest

from math import factorial, pow
from app.n_of_1 import randomise_n_of_1_schedule, permutate, block, shuffled_block


@pytest.mark.parametrize("treatments,expected", [(2, [['A', 'B'], ['B', 'A']]),
                                                 (3, [['A', 'B', 'C'],
                                                      ['A', 'C', 'B'],
                                                      ['B', 'A', 'C'],
                                                      ['B', 'C', 'A'],
                                                      ['C', 'A', 'B'],
                                                      ['C', 'B', 'A']])])
def test_permutations(treatments, expected):
    actual = permutate(treatments)
    assert len(actual) == factorial(treatments)
    assert actual == expected


@pytest.mark.parametrize("cycles,treatments,expected", [(2, 2, [[['A', 'B'], ['A', 'B']],
                                                                [['A', 'B'], ['B', 'A']],
                                                                [['B', 'A'], ['A', 'B']],
                                                                [['B', 'A'], ['B', 'A']]])])
def test_block_and_shuffle(cycles, treatments, expected):
    schedules = block(cycles, treatments)
    assert len(schedules) == pow(factorial(treatments), cycles)
    assert schedules == expected

    block_generator = shuffled_block(cycles, treatments)
    for _ in range(3):
        assert len(next(block_generator)) == pow(factorial(treatments), cycles)


@pytest.mark.parametrize("patients,cycles,treatments", [(4, 2, 2), (40, 3, 2)])
def test_randomise_schedule(patients, cycles, treatments):
    schedule = randomise_n_of_1_schedule(patients, cycles, treatments)
    assert len(schedule) == patients
    assert len(schedule[0]) == cycles
    assert len(schedule[0][0]) == treatments
    assert schedule[0][0][0].isalpha()
