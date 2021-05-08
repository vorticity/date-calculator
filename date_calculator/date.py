from enum import Enum
from dataclasses import dataclass


DAYS_LEAP_YEAR = 366
DAYS_NON_LEAP_YEAR = 365
YEAR_LOWER_BOUND = 1901
YEAR_UPPER_BOUND = 2999


class Month(Enum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12


@dataclass(frozen=True, eq=True)
class Date:
    year: int = YEAR_LOWER_BOUND
    month: Month = Month.JANUARY
    day: int = 1

    def is_same_year(self, other) -> bool:
        return self.year == other.year

    def is_same_month(self, other) -> bool:
        return self.month == other.month

    def days_till_end_of_month(self) -> int:
        return days_per_month(self.month, self.year) - self.day

    @classmethod
    def from_string(cls, string: str):
        # TODO: regex and exception handling
        tokens = list(map(int, string.split("/")))
        return cls(year=tokens[2], month=Month(tokens[1]), day=tokens[0])

    def __lt__(self, other):
        if self.year < other.year:
            return True
        if self.month.value < other.month.value:
            return True
        if self.day < other.day:
            return True
        return False


def is_exactly_divisible(numerator: int, denominator: int) -> bool:
    return numerator % denominator == 0


def is_centurial_year(year: int) -> bool:
    return True if is_exactly_divisible(year, 100) else False


def is_leap_year(year: int) -> bool:
    if is_centurial_year(year):
        if is_exactly_divisible(year, 400):
            return True
        else:
            return False
    return True if is_exactly_divisible(year, 4) else False


def days_per_month(month: Month, year: int) -> int:
    if month in (Month.SEPTEMBER, Month.APRIL, Month.JUNE, Month.NOVEMBER):
        return 30
    if month == Month.FEBRUARY:
        if is_leap_year(year):
            return 29
        else:
            return 28
    return 31


def days_in_month_range_inclusive(start_month: Month, end_month: Month, year: int) -> int:
    days = 0
    for month_number in range(start_month.value, end_month.value + 1):
        days += days_per_month(Month(month_number), year)
    return days


def days_in_fully_elapsed_year_range(start_year: int, end_year: int) -> int:
    days = 0
    for year in range(start_year + 1, end_year):
        days += DAYS_LEAP_YEAR if is_leap_year(year) else DAYS_NON_LEAP_YEAR
    return days


def days_elapsed(date1: Date, date2: Date) -> int:
    """From start_date to end_date"""
    start_date, end_date = sorted((date1, date2))

    if start_date.is_same_year(end_date):
        if start_date.is_same_month(end_date):
            return end_date.day - start_date.day
        else:
            return (
                days_in_month_range_inclusive(start_date.month, end_date.month, start_date.year)
                - start_date.day
                - end_date.days_till_end_of_month()
            )

    left = (
        days_in_month_range_inclusive(start_date.month, Month.DECEMBER, start_date.year)
        - start_date.day
    )
    middle = days_in_fully_elapsed_year_range(start_date.year, end_date.year)
    right = (
        days_in_month_range_inclusive(Month.JANUARY, end_date.month, end_date.year)
        - end_date.days_till_end_of_month()
    )
    return left + middle + right


def days_fully_elapsed_between(date1: Date, date2: Date) -> int:
    return 0 if date1 == date2 else days_elapsed(date1, date2) - 1
