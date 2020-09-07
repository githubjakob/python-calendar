# python-calendar

This software allows users to book an appointment, choosing from a list of available time slots.

The core feature allows you to calculate the free available time slots from a calendar that already contains appointments, like this:

```
calendar = Calendar()

calendar.set_opening_times('THURSDAY', '08:00:00', '18:00:00')

appointment1 = Appointment(
    start='2020-10-01T10:00:00', end='2020-10-01T12:00:00')
calendar.add_appointment(appointment1)

free_periods = calendar.get_free_periods_for_date(date.fromisoformat('2020-10-01'))

assert len(free_periods) == 2
assert Period.fromIsoFormat(
    '2020-10-01T08:00:00', '2020-10-01T10:00:00') in free_periods
assert Period.fromIsoFormat(
    '2020-10-01T12:00:00', '2020-10-01T18:00:00') in free_periods

``` 

It works on the concept of a `Period` (which is defined by a start and end timestamp) and defines various operations on them. 

For simplictiy let's denote a `Period` from 2pm to 3pm by `P(2,3)`. 

You can `subtract` a Period A from a Period B which results in the time that is included in B but not in A, e.g.
``` 
P(1,6) - P(2,3) = [P(1,2), P(3,6)]
``` 

You can also `add` a Period A to a Period B which results in the time which that is included in both Periods, e.g.
``` 
P(1,2) + P(2,3) = [P(1,3)]
``` 

Building upon these operations, we can also build higher order operations, like subtracting a list of Periods A1.. from a PeriodB, e.g.
```
P(1,6) - [P(4,5), P(5,6)] = [P(1,4)]
``` 

Other operations include
- checking if Periods `overlap`
- checking if a Period is `contained` in another Period
- `merging` Periods if they overlap, e.g. `merge(P(1,2),P(2,3)) = P(1,3)`

## Setup

Install venv

```
python3 -m pip install --user virtualenv

py -m pip install --user virtualenv

```

Create venv

```
python3 -m venv .venv

py -m venv env
```

Activate venv

```
.venv\Scripts\activate.bat

source .venv/bin/activate
```

Install dependencies

```
pip install -r requirements.txt
```

Leave venv

```
deactivate
```

## Tests

```
python -m pytest

show console log
python -m pytest -s
```
