import pytest

from date_calculator.constants import Month
from date_calculator.models import Date


data_days_fully_elapsed_to = [
    ("03/08/2018", "03/08/2018", 0),
    ("03/08/2018", "04/08/2018", 0),
    ("01/01/2000", "03/01/2000", 1),
    ("02/06/1983", "22/06/1983", 19),
    ("04/07/1984", "25/12/1984", 173),
    ("03/01/1989", "03/08/1983", 1979),
    ("31/12/1999", "01/01/2001", 366),
    ("01/01/1901", "01/01/1913", 4382),
    ("01/01/1901", "01/01/2001", 36524),
    ("01/01/1901", "31/12/2001", 36888),
    ("01/01/1901", "31/12/2501", 219509),
    ("01/01/1901", "31/12/2999", 401400),
]


@pytest.mark.parametrize("date1, date2, expected", data_days_fully_elapsed_to)
def test_days_fully_elapsed_to(date1, date2, expected):
    assert Date.from_string(date1).days_fully_elapsed_to(Date.from_string(date2)) == expected


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


def test_year_is_out_of_range():
    with pytest.raises(ValueError, match=".*Year out of range: .*"):
        date = Date.from_string("08/05/1900")
    with pytest.raises(ValueError, match=".*Year out of range: .*"):
        date = Date.from_string("08/05/3000")


def test_day_is_out_of_range():
    with pytest.raises(ValueError, match=".*Day out of range: .*"):
        date = Date.from_string("00/05/2021")
    with pytest.raises(ValueError, match=".*Day out of range: .*"):
        date = Date.from_string("32/05/2021")


def test_days_till_end_of_year():
    assert Date.from_string("31/12/1999").days_till_end_of_year() == 0
    assert Date.from_string("01/01/2000").days_till_end_of_year() == 365
    assert Date.from_string("01/01/1901").days_till_end_of_year() == 364


def test_days_since_start_of_year():
    assert Date.from_string("31/12/2001").days_since_start_of_year() == 365
    assert Date.from_string("01/01/2001").days_since_start_of_year() == 1