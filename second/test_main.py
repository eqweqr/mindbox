from culculate_figure import calculate_figure
import pytest
import random
from datetime import datetime
import math

@pytest.fixture
def get_seed():
    random.seed(datetime.timestamp(datetime.now()))


def test_round_correct_values():
    tc = []
    for i in range(10):
        r = random.random()*random.randint(1, 3)
        tc.append((r, math.pi*r**2))

    for test in tc:
        assert test[1] == calculate_figure(test[0])


def test_round_with_negative():
    tc = []
    for i in range(10):
        r = -random.random()*random.randint(1, 3)
        tc.append(r)

    for test in tc:
        with pytest.raises(ValueError):
            calculate_figure(test)


def foo(a,b,c):
    p = (a+b+c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))


def test_trianle_correct():
    tc = [(1, 2, 2.7, foo(1,2,2.7)),
          (2, 5, 6, foo(2, 5, 6)),
          (1.5, 23.1, 23, foo(1.5, 23.1, 23))
        ]
    for test in tc:
        assert test[3] == calculate_figure(test[0], test[1], test[2])
    

def test_triangle_with_neg():
    tc = [(1, -2, 2.5)]    
    for test in tc:
        with pytest.raises(ValueError):
            calculate_figure(test[0], test[1], test[2])


def test_triangle_incorrect():
    tc = [(1, 2, 3)]
    
    for test in tc:
        with pytest.raises(ValueError):
            calculate_figure(test[0], test[1], test[2])
