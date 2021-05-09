# date-calculator
Technical exercise: TDD implementation of a Date class written from scratch, without depending on datetime or any third party libraries.

As used by the [date-calculator-cli](https://github.com/vorticity/date-calculator-cli) command line interface.

## Installation
Clone this repository, navigate to the repository root and run:
```bash
poetry install
```

## Testing
Tests are implemented with pytest. Navigate to the repository root and run:
```bash
poetry shell
pytest
```

## Usage
A command line interface is provided for your convenience: [date-calculator-cli](https://github.com/vorticity/date-calculator-cli).

Should you wish to use the date_calculator library and Date class in your own code, please refer the example below:
```python

>>>from date_calculator.constants import Month
>>>from date_calculator.models import Date
>>>start = Date(year=2021, month=Month.MAY, day=7)
>>>end = Date(year=2021, month=Month.MAY, day=9)
>>>print(start.days_fully_elapsed_to(end))
1
>>>
```

## References

* https://en.wikipedia.org/wiki/Thirty_Days_Hath_September
* https://en.wikipedia.org/wiki/Gregorian_calendar
* https://en.wikipedia.org/wiki/Leap_year
* https://docs.pytest.org/en/6.2.x/parametrize.html
* https://docs.python.org/3/library/functools.html#functools.total_ordering
* https://docs.python.org/3/library/dataclasses.html
* https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code
