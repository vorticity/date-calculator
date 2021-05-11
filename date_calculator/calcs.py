from date_calculator.constants import (
    Month,
    DAYS_LEAP_YEAR,
    DAYS_NON_LEAP_YEAR,
    YEAR_LOWER_BOUND,
    YEAR_UPPER_BOUND,
)


def is_exactly_divisible(dividend: int, divisor: int) -> bool:
    return dividend % divisor == 0


def is_centurial_year(year: int) -> bool:
    return is_exactly_divisible(year, 100)


def is_leap_year(year: int) -> bool:
    if is_centurial_year(year):
        return is_exactly_divisible(year, 400)
    return is_exactly_divisible(year, 4)


def days_per_month(month: Month, year: int) -> int:
    if month in (Month.SEPTEMBER, Month.APRIL, Month.JUNE, Month.NOVEMBER):
        return 30
    if month == Month.FEBRUARY:
        if is_leap_year(year):
            return 29
        return 28
    return 31


def days_in_month_range_inclusive(start_month: Month, end_month: Month,
                                  year: int) -> int:
    days = 0
    for month_number in range(start_month.value, end_month.value + 1):
        days += days_per_month(Month(month_number), year)
    return days


def _first_leap_year_offset(start_year: int) -> int:
    """0 based index of first leap year relative to start year"""
    for offset, year in enumerate(range(start_year, start_year + 4)):
        if is_leap_year(year):
            return offset


def leap_years_in_range(start_year: int, end_year: int) -> int:
    offset = _first_leap_year_offset(start_year)
    years_in_range = end_year - start_year + 1
    if offset > years_in_range - 1:
        return 0
    leap_years_in_range = years_in_range // 4
    remainder = years_in_range % 4
    if offset <= remainder:
        leap_years_in_range += 1
    return leap_years_in_range


def days_in_fully_elapsed_year_range(start_year: int, end_year: int) -> int:
    """Naive implementation. Replace this with something better to handle a larger range."""
    if start_year < YEAR_LOWER_BOUND or end_year < YEAR_LOWER_BOUND:
        raise ValueError("Year lower bound exceeded: {} {}".format(
            start_year, end_year))
    if start_year > YEAR_UPPER_BOUND or end_year > YEAR_UPPER_BOUND:
        raise ValueError("Year upper bound exceeded: {} {}".format(
            start_year, end_year))
    total_years = end_year - start_year - 1
    leap_years = leap_years_in_range(start_year + 1, end_year)
    return DAYS_LEAP_YEAR * leap_years + (total_years - leap_years) * DAYS_NON_LEAP_YEAR
