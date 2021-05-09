from enum import Enum


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
