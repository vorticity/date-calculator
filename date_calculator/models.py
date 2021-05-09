from dataclasses import dataclass
from functools import total_ordering

from date_calculator.calcs import (
    days_per_month,
    days_in_month_range_inclusive,
    days_in_fully_elapsed_year_range,
)
from date_calculator.constants import Month, YEAR_LOWER_BOUND, YEAR_UPPER_BOUND


@total_ordering
@dataclass(frozen=True, eq=True)
class Date:
    year: int = YEAR_LOWER_BOUND
    month: Month = Month.JANUARY
    day: int = 1

    def days_till_end_of_month(self) -> int:
        return days_per_month(self.month, self.year) - self.day

    def days_till_end_of_year(self) -> int:
        return days_in_month_range_inclusive(self.month, Month.DECEMBER, self.year) - self.day

    def days_since_start_of_year(self) -> int:
        return (
            days_in_month_range_inclusive(Month.JANUARY, self.month, self.year)
            - self.days_till_end_of_month()
        )

    def days_elapsed_to(self, other: "Date") -> int:
        start_date, end_date = sorted((self, other))

        if start_date.is_same_year_as(end_date):
            if start_date.is_same_month_as(end_date):
                return end_date.day - start_date.day
            return (
                days_in_month_range_inclusive(start_date.month, end_date.month, start_date.year)
                - start_date.day
                - end_date.days_till_end_of_month()
            )

        return (
            start_date.days_till_end_of_year()
            + days_in_fully_elapsed_year_range(start_date.year, end_date.year)
            + end_date.days_since_start_of_year()
        )

    def days_fully_elapsed_to(self, other: "Date") -> int:
        return 0 if self == other else self.days_elapsed_to(other) - 1

    def is_same_year_as(self, other: "Date") -> bool:
        return self.year == other.year

    def is_same_month_as(self, other: "Date") -> bool:
        return self.month == other.month

    @classmethod
    def from_string(cls, string: str) -> "Date":
        """Expected date string format is: DD/MM/YYYY"""
        tokens = list(map(int, string.split("/")))
        if tokens[2] < YEAR_LOWER_BOUND or tokens[2] > YEAR_UPPER_BOUND:
            raise ValueError("Year out of range: {}".format(tokens[2]))
        if tokens[0] < 1 or tokens[0] > days_per_month(Month(tokens[1]), tokens[2]):
            raise ValueError("Day out of range: {}".format(tokens[0]))
        return cls(year=tokens[2], month=Month(tokens[1]), day=tokens[0])

    def __lt__(self, other) -> bool:
        return (self.year, self.month.value, self.day) < (other.year, other.month.value, other.day)
