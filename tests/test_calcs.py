import pytest

from date_calculator.calcs import (
    days_in_fully_elapsed_year_range,
    days_in_month_range_inclusive,
    days_per_month,
    is_leap_year,
    leap_years_in_range
)
from date_calculator.constants import Month


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


data_days_per_month = [
    (Month.JANUARY, 1999, 31),
    (Month.FEBRUARY, 1999, 28),
    (Month.MARCH, 1999, 31),
    (Month.APRIL, 1999, 30),
    (Month.MAY, 1999, 31),
    (Month.JUNE, 1999, 30),
    (Month.JULY, 1999, 31),
    (Month.AUGUST, 1999, 31),
    (Month.SEPTEMBER, 1999, 30),
    (Month.OCTOBER, 1999, 31),
    (Month.NOVEMBER, 1999, 30),
    (Month.DECEMBER, 1999, 31),
    (Month.JANUARY, 2000, 31),
    (Month.FEBRUARY, 2000, 29),
    (Month.MARCH, 2000, 31),
    (Month.APRIL, 2000, 30),
    (Month.MAY, 2000, 31),
    (Month.JUNE, 2000, 30),
    (Month.JULY, 2000, 31),
    (Month.AUGUST, 2000, 31),
    (Month.SEPTEMBER, 2000, 30),
    (Month.OCTOBER, 2000, 31),
    (Month.NOVEMBER, 2000, 30),
    (Month.DECEMBER, 2000, 31),
]


@pytest.mark.parametrize("month, year, expected", data_days_per_month)
def test_days_per_month(month, year, expected):
    """
    Thirty days hath September,
    April, June, and November,
    All the rest have thirty-one,
    But February's twenty-eight,
    The leap year, which comes once in four,
    Gives February one day more.
    """
    assert days_per_month(month, year) == expected


def test_days_in_fully_elapsed_year_range():
    assert days_in_fully_elapsed_year_range(1998, 2000) == 365
    assert days_in_fully_elapsed_year_range(1999, 2000) == 0
    assert days_in_fully_elapsed_year_range(1999, 2001) == 366
    assert days_in_fully_elapsed_year_range(1999, 2002) == 731


def test_leap_years_in_range():
    assert leap_years_in_range(2000, 2000) == 1
    assert leap_years_in_range(2000, 2001) == 1
    assert leap_years_in_range(2001, 2001) == 0
    assert leap_years_in_range(2001, 2002) == 0
    assert leap_years_in_range(2001, 2003) == 0
    assert leap_years_in_range(2001, 2004) == 1
    assert leap_years_in_range(2000, 2004) == 2
    assert leap_years_in_range(2000, 2008) == 3
    assert leap_years_in_range(2000, 2009) == 3
    assert leap_years_in_range(2001, 2009) == 2
    assert leap_years_in_range(2001, 2010) == 2
