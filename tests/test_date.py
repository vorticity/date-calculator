import pytest

from date_calculator.date import (
    days_fully_elapsed_between,
    days_per_month,
    is_leap_year,
    days_in_month_range_inclusive,
    Date,
    Month,
)


def test_days_in_month_range():
    assert days_in_month_range_inclusive(Month.JANUARY, Month.DECEMBER, 2000) == 366
    assert days_in_month_range_inclusive(Month.JANUARY, Month.DECEMBER, 2001) == 365


def test_date_defaults():
    date = Date()
    assert date.year == 1901
    assert date.month == Month.JANUARY
    assert date.day == 1


def test_date_equality():
    date1 = Date(2000, Month.JANUARY, 1)
    date2 = Date(2000, Month.JANUARY, 1)
    assert date1 == date2
    date3 = Date(2000, Month.JANUARY, 2)
    assert date2 != date3


def test_date_comparison():
    assert Date(1999, Month.DECEMBER, 31) < Date(2000, Month.JANUARY, 1)
    assert Date(2000, Month.JANUARY, 1) > Date(1999, Month.DECEMBER, 31)
    assert Date(2001, Month.JANUARY, 26) < Date(2001, Month.FEBRUARY, 14)
    assert Date(2001, Month.APRIL, 1) > Date(2001, Month.JANUARY, 1)


def test_date_from_string():
    date = Date.from_string("08/05/2021")
    assert date.year == 2021
    assert date.month == Month.MAY
    assert date.day == 8


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


data_days_fully_elapsed_between = [
    ("03/08/2018", "03/08/2018", 0),
    ("03/08/2018", "04/08/2018", 0),
    ("01/01/2000", "03/01/2000", 1),
    ("02/06/1983", "22/06/1983", 19),
    ("04/07/1984", "25/12/1984", 173),
    ("03/01/1989", "03/08/1983", 1979),
    ("01/01/1901", "31/12/2999", 401400),
]


@pytest.mark.parametrize("date1, date2, expected", data_days_fully_elapsed_between)
def test_days_fully_elapsed_between(date1, date2, expected):
    assert days_fully_elapsed_between(Date.from_string(date1), Date.from_string(date2)) == expected
