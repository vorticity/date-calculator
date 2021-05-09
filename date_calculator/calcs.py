from date_calculator.constants import Month, DAYS_LEAP_YEAR, DAYS_NON_LEAP_YEAR


def is_exactly_divisible(numerator: int, denominator: int) -> bool:
    return numerator % denominator == 0


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
    days = 0
    for year in range(start_year + 1, end_year):
        days += DAYS_LEAP_YEAR if is_leap_year(year) else DAYS_NON_LEAP_YEAR
    return days
