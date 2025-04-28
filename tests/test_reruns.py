import pytest
import random

@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_reruns():
    assert  random.choice([True, False])



PLATFORM = "Linux"

@pytest.mark.flaky(reruns=3, reruns_delay=2, condition=PLATFORM == 'Windows')
def test_reruns_with_condition():
    assert  random.choice([True, False])


