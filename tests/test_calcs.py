import pytest

from date_calculator.calcs import (
    days_in_month_range_inclusive,
    days_per_month,
    is_leap_year,
)
from date_calculator.contants import Month


data_is_leap_year = [
    (1600, True),
    (1604, True),
    (1608, True),
    (1700, False),
    (1800, False),
    (1900, False),
    (2000, True),
    (2001, False),
    (2002, False),
    (2003, False),
    (2004, True),
    (2008, True),
    (2100, False),
    (2200, False),
    (2300, False),
    (2400, True),
    (2404, True),
    (2408, True),
    (2500, False),
    (2600, False),
    (2700, False),
    (2800, True),
    (2804, True),
    (2808, True),
    (2900, False),
    (3000, False),
]


@pytest.mark.parametrize("year, expected", data_is_leap_year)
def test_is_leap_year(year, expected):
    """
    Every year that is exactly divisible by four is a leap year, except for
    years that are exactly divisible by 100, but these centurial years are
    leap years if they are exactly divisible by 400. For example, the years
    1700, 1800, and 1900 are not leap years, but the years 1600 and 2000 are.
    """
    assert is_leap_year(year) == expected


def test_days_in_month_range():
    assert days_in_month_range_inclusive(Month.JANUARY, Month.JANUARY, 2000) == days_per_month(
        Month.JANUARY, 2000
    )
    assert days_in_month_range_inclusive(Month.JANUARY, Month.DECEMBER, 2000) == 366
    assert days_in_month_range_inclusive(Month.JANUARY, Month.DECEMBER, 2001) == 365


def test_days_per_month():
    """
    Thirty days hath September,
    April, June, and November,
    All the rest have thirty-one,
    But February's twenty-eight,
    The leap year, which comes once in four,
    Gives February one day more.
    """
    assert days_per_month(Month.SEPTEMBER, 2000) == 30
    assert days_per_month(Month.APRIL, 2000) == 30
    assert days_per_month(Month.JUNE, 2000) == 30
    assert days_per_month(Month.NOVEMBER, 2000) == 30
    assert days_per_month(Month.FEBRUARY, 1999) == 28
    assert days_per_month(Month.FEBRUARY, 2000) == 29
