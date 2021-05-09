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


def days_in_month_range_inclusive(start_month: Month, end_month: Month, year: int) -> int:
    days = 0
    for month_number in range(start_month.value, end_month.value + 1):
        days += days_per_month(Month(month_number), year)
    return days


def days_in_fully_elapsed_year_range(start_year: int, end_year: int) -> int:
    """Naive implementation. Replace this with something better to handle a larger range."""
    if start_year < YEAR_LOWER_BOUND or end_year < YEAR_LOWER_BOUND:
        raise ValueError("Year lower bound exceeded: {} {}".format(start_year, end_year))
    if start_year > YEAR_UPPER_BOUND or end_year > YEAR_UPPER_BOUND:
        raise ValueError("Year upper bound exceeded: {} {}".format(start_year, end_year))
    days = 0
    for year in range(start_year + 1, end_year):
        days += DAYS_LEAP_YEAR if is_leap_year(year) else DAYS_NON_LEAP_YEAR
    return days
