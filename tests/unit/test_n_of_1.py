import pytest

from app.n_of_1 import randomise_n_of_1_schedule


@pytest.mark.parametrize("patients", [1, 10, 40])
@pytest.mark.parametrize("cycles", [3, 8, 12])
@pytest.mark.parametrize("treatments", [1, 2, 4])
def test_randomise_schedule(patients, cycles, treatments):
    schedule = randomise_n_of_1_schedule(patients, cycles, treatments)
    assert len(schedule) == patients
    assert len(schedule[0]) == cycles
    assert len(schedule[0][0]) == treatments
    assert schedule[0][0][0].isalpha()
