# import math


def minimum(list):
    # return min(list)
    # min = math.inf
    min = list[0]
    for i in list:
        min = i if i < min else min
    return min


def test_minimum():
    assert minimum( [5, 9, 3, 19, 70, 8, 100, 2, 35, 27]) == 2