import pytest
from data_analysis.profit_analysis import sell_today


@pytest.mark.parametrize("a,b,expect", [(0.1, 100, 0), (100, 0.1, 1)])
def tests_sell_today(a, b, expect):
    assert sell_today(a, b, 1, 1) == expect


def main():
    tests_sell_today()
    return
