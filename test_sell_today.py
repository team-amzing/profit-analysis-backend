import pytest
from data_analysis.profit_analysis import sell_today


@pytest.mark.parametrize("a,b,c,d,expect", [(0.1, 100, 1, 1, 0), (100, 0.1, 1, 1, 1)])
def tests_sell_today(a, b, c, d, expect):
    assert sell_today(a, b, c, d) == expect
