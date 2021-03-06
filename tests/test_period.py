from src.entities.period import Period
from datetime import datetime, timedelta
import time


def test_period():
    start = datetime.fromisoformat('2020-10-01T12:00:00')
    end = datetime.fromisoformat('2020-10-01T13:00:00')
    period = Period(start, end)
    assert period.start == datetime(2020, 10, 1, 12, 0) and period.end == datetime(2020, 10, 1, 13, 0) 


def test_period_get_duration():
    start = datetime.fromisoformat('2020-10-01T12:00:00')
    end = datetime.fromisoformat('2020-10-01T13:00:00')
    period = Period(start, end)
    duration = period.get_duration()
    assert duration == timedelta(hours=1)


def test_period_is_overlapping():
    start = datetime.fromisoformat('2020-10-01T12:00:00')
    end = datetime.fromisoformat('2020-10-01T13:00:00')
    period1 = Period(start, end)
    period2 = Period(start, end)

    is_overlapping = period1.is_overlapped(period2)

    assert is_overlapping == True


def test_period_is_overlapping_2():
    start1 = datetime.fromisoformat('2020-10-01T12:00:00')
    end1 = datetime.fromisoformat('2020-10-01T13:00:00')
    period1 = Period(start1, end1)

    start2 = datetime.fromisoformat('2000-10-01T12:00:00')
    end2 = datetime.fromisoformat('2000-10-01T13:00:00')
    period2 = Period(start2, end2)

    is_overlapping = period1.is_overlapped(period2)

    assert is_overlapping == False


def test_period_is_overlapping_3():
    start1 = datetime.fromisoformat('2020-10-01T12:00:00')
    end1 = datetime.fromisoformat('2020-10-01T18:00:00')
    period1 = Period(start1, end1)

    start2 = datetime.fromisoformat('2020-10-01T17:00:00')
    end2 = datetime.fromisoformat('2020-10-01T20:00:00')
    period2 = Period(start2, end2)

    is_overlapping = period1.is_overlapped(period2)

    assert is_overlapping == True


def test_period_is_overlapping_4():
    start1 = datetime.fromisoformat('2020-10-01T12:00:00')
    end1 = datetime.fromisoformat('2020-10-01T18:00:00')
    period1 = Period(start1, end1)

    start2 = datetime.fromisoformat('2020-10-01T09:00:00')
    end2 = datetime.fromisoformat('2020-10-01T12:30:00')
    period2 = Period(start2, end2)

    is_overlapping = period1.is_overlapped(period2)

    assert is_overlapping == True


def test_period_is_overlapping_5():
    start1 = datetime.fromisoformat('2020-10-01T12:00:00')
    end1 = datetime.fromisoformat('2020-10-01T15:00:00')
    period1 = Period(start1, end1)

    start2 = datetime.fromisoformat('2020-10-01T15:00:00')
    end2 = datetime.fromisoformat('2020-10-01T18:00:00')
    period2 = Period(start2, end2)

    is_overlapping = period1.is_overlapped(period2)

    assert is_overlapping == True


def test_period_get_overlapping():
    start1 = datetime.fromisoformat('2020-10-01T12:00:00')
    end1 = datetime.fromisoformat('2020-10-01T18:00:00')
    period1 = Period(start1, end1)

    start2 = datetime.fromisoformat('2020-10-01T09:00:00')
    end2 = datetime.fromisoformat('2020-10-01T12:30:00')
    period2 = Period(start2, end2)

    overlapping = period1.get_overlapped_period(period2)

    expected_start = datetime.fromisoformat('2020-10-01T12:00:00')
    expected_end = datetime.fromisoformat('2020-10-01T12:30:00')
    assert overlapping == Period(expected_start, expected_end)


def test_period_add_not_overlapping():
    start1 = datetime.fromisoformat('2000-10-01T12:00:00')
    end1 = datetime.fromisoformat('2000-10-01T18:00:00')
    period1 = Period(start1, end1)

    start2 = datetime.fromisoformat('2020-10-01T09:00:00')
    end2 = datetime.fromisoformat('2020-10-01T12:30:00')
    period2 = Period(start2, end2)

    added = period1 + period2

    assert len(added) == 2
    assert period1 in added
    assert period2 in added


def test_period_add_overlapping():
    start1 = datetime.fromisoformat('2020-10-01T12:00:00')
    end1 = datetime.fromisoformat('2020-10-01T16:00:00')
    period1 = Period(start1, end1)

    start2 = datetime.fromisoformat('2020-10-01T12:00:00')
    end2 = datetime.fromisoformat('2020-10-01T18:00:00')
    period2 = Period(start2, end2)

    added = period1 + period2

    expected_start = datetime.fromisoformat('2020-10-01T12:00:00')
    expected_end = datetime.fromisoformat('2020-10-01T18:00:00')

    expected_period = Period(expected_start, expected_end)

    assert len(added) == 1
    assert expected_period in added


def test_period_add_overlapping_2():
    start1 = datetime.fromisoformat('2020-10-01T12:00:00')
    end1 = datetime.fromisoformat('2020-10-01T18:00:00')
    period1 = Period(start1, end1)

    start2 = datetime.fromisoformat('2020-10-01T10:00:00')
    end2 = datetime.fromisoformat('2020-10-01T16:00:00')
    period2 = Period(start2, end2)

    added = period1 + period2

    expected_start = datetime.fromisoformat('2020-10-01T10:00:00')
    expected_end = datetime.fromisoformat('2020-10-01T18:00:00')

    expected_period = Period(expected_start, expected_end)

    assert len(added) == 1
    assert expected_period in added


def test_period_subtract_not_overlapping():
    start1 = datetime.fromisoformat('2000-10-01T12:00:00')
    end1 = datetime.fromisoformat('2000-10-01T16:00:00')
    period1 = Period(start1, end1)

    start2 = datetime.fromisoformat('2020-10-01T12:00:00')
    end2 = datetime.fromisoformat('2020-10-01T18:00:00')
    period2 = Period(start2, end2)

    subtracted = period1 - period2

    assert len(subtracted) == 1
    assert period1 in subtracted


def test_period_subtract_overlapping_1():
    start1 = datetime.fromisoformat('2020-10-01T12:00:00')
    end1 = datetime.fromisoformat('2020-10-01T16:00:00')
    period1 = Period(start1, end1)

    start2 = datetime.fromisoformat('2020-10-01T15:00:00')
    end2 = datetime.fromisoformat('2020-10-01T18:00:00')
    period2 = Period(start2, end2)

    subtracted = period1 - period2

    expected_start = datetime.fromisoformat('2020-10-01T12:00:00')
    expected_end = datetime.fromisoformat('2020-10-01T15:00:00')

    expected_period = Period(expected_start, expected_end)

    assert len(subtracted) == 1
    assert expected_period in subtracted


def test_period_subtract_overlapping_2():
    start1 = datetime.fromisoformat('2020-10-01T16:00:00')
    end1 = datetime.fromisoformat('2020-10-01T18:00:00')
    period1 = Period(start1, end1)

    start2 = datetime.fromisoformat('2020-10-01T12:00:00')
    end2 = datetime.fromisoformat('2020-10-01T17:00:00')
    period2 = Period(start2, end2)

    subtracted = period1 - period2

    expected_start = datetime.fromisoformat('2020-10-01T17:00:00')
    expected_end = datetime.fromisoformat('2020-10-01T18:00:00')

    expected_period = Period(expected_start, expected_end)

    assert len(subtracted) == 1
    assert expected_period in subtracted


def test_period_subtract_overlapping_3():
    start1 = datetime.fromisoformat('2020-10-01T10:00:00')
    end1 = datetime.fromisoformat('2020-10-01T18:00:00')
    period1 = Period(start1, end1)

    start2 = datetime.fromisoformat('2020-10-01T16:00:00')
    end2 = datetime.fromisoformat('2020-10-01T22:00:00')
    period2 = Period(start2, end2)

    subtracted = period1 - period2

    expected_start = datetime.fromisoformat('2020-10-01T10:00:00')
    expected_end = datetime.fromisoformat('2020-10-01T16:00:00')

    expected_period = Period(expected_start, expected_end)

    assert len(subtracted) == 1
    assert expected_period in subtracted


def test_period_subtract_contains():
    start1 = datetime.fromisoformat('2020-10-01T10:00:00')
    end1 = datetime.fromisoformat('2020-10-01T18:00:00')
    period1 = Period(start1, end1)

    start2 = datetime.fromisoformat('2020-10-01T14:00:00')
    end2 = datetime.fromisoformat('2020-10-01T15:00:00')
    period2 = Period(start2, end2)

    subtracted = period1 - period2

    expected_start1 = datetime.fromisoformat('2020-10-01T10:00:00')
    expected_end1 = datetime.fromisoformat('2020-10-01T14:00:00')

    expected_period = Period(expected_start1, expected_end1)

    expected_start2 = datetime.fromisoformat('2020-10-01T15:00:00')
    expected_end2 = datetime.fromisoformat('2020-10-01T18:00:00')

    expected_period_2 = Period(expected_start2, expected_end2)

    assert len(subtracted) == 2
    assert expected_period in subtracted
    assert expected_period_2 in subtracted


def test_period_contains():
    start1 = datetime.fromisoformat('2000-10-01T10:00:00')
    end1 = datetime.fromisoformat('2000-10-01T18:00:00')
    period1 = Period(start1, end1)

    start2 = datetime.fromisoformat('2020-10-01T16:00:00')
    end2 = datetime.fromisoformat('2020-10-01T17:00:00')
    period2 = Period(start2, end2)

    is_contained = period1.contains(period2)

    assert is_contained == False


def test_period_contains_2():
    start1 = datetime.fromisoformat('2020-10-01T10:00:00')
    end1 = datetime.fromisoformat('2020-10-01T18:00:00')
    period1 = Period(start1, end1)

    start2 = datetime.fromisoformat('2020-10-01T16:00:00')
    end2 = datetime.fromisoformat('2020-10-01T17:00:00')
    period2 = Period(start2, end2)

    is_contained = period1.contains(period2)

    assert is_contained == True


def test_period_contains_3():
    start1 = datetime.fromisoformat('2020-10-01T10:00:00')
    end1 = datetime.fromisoformat('2020-10-01T18:00:00')
    period1 = Period(start1, end1)

    start2 = datetime.fromisoformat('2020-10-01T17:00:00')
    end2 = datetime.fromisoformat('2020-10-01T22:00:00')
    period2 = Period(start2, end2)

    is_contained = period1.contains(period2)

    assert is_contained == False


def test_period_subtract_contained():
    start1 = datetime.fromisoformat('2020-10-01T10:00:00')
    end1 = datetime.fromisoformat('2020-10-01T18:00:00')
    period1 = Period(start1, end1)

    start2 = datetime.fromisoformat('2020-10-01T13:00:00')
    end2 = datetime.fromisoformat('2020-10-01T14:00:00')
    period2 = Period(start2, end2)

    subtracted = period1 - period2

    expected_start_1 = datetime.fromisoformat('2020-10-01T10:00:00')
    expected_end_1 = datetime.fromisoformat('2020-10-01T13:00:00')
    expected_first = Period(expected_start_1, expected_end_1)

    expected_start_2 = datetime.fromisoformat('2020-10-01T14:00:00')
    expected_end_2 = datetime.fromisoformat('2020-10-01T18:00:00')
    expected_second = Period(expected_start_2, expected_end_2)

    assert len(subtracted) == 2
    assert expected_first in subtracted
    assert expected_second in subtracted


def test_period_subtract_contained_2():
    start1 = datetime.fromisoformat('2020-10-01T14:00:00')
    end1 = datetime.fromisoformat('2020-10-01T15:00:00')
    period1 = Period(start1, end1)

    start2 = datetime.fromisoformat('2020-10-01T10:00:00')
    end2 = datetime.fromisoformat('2020-10-01T18:00:00')
    period2 = Period(start2, end2)

    subtracted = period1 - period2

    assert len(subtracted) == 0


def test_subtract():
    period = Period.fromIsoFormat('2000-10-01T10:00:00', '2000-10-01T14:00:00')

    subtracted = period.subtract([])

    assert len(subtracted) == 1
    assert period in subtracted


def test_subtract_2():
    period = Period.fromIsoFormat('2000-10-01T10:00:00', '2000-10-01T18:00:00')

    subtract = Period.fromIsoFormat(
        '2000-10-01T14:00:00', '2000-10-01T15:00:00')

    subtracted = period.subtract([subtract])

    expected_1 = Period.fromIsoFormat(
        '2000-10-01T10:00:00', '2000-10-01T14:00:00')
    expected_2 = Period.fromIsoFormat(
        '2000-10-01T15:00:00', '2000-10-01T18:00:00')

    assert len(subtracted) == 2
    assert expected_1 in subtracted
    assert expected_2 in subtracted


def test_subtract_3():
    period = Period.fromIsoFormat('2000-10-01T10:00:00', '2000-10-01T22:00:00')

    subtract_1 = Period.fromIsoFormat(
        '2000-10-01T14:00:00', '2000-10-01T15:00:00')

    subtract_2 = Period.fromIsoFormat(
        '2000-10-01T17:00:00', '2000-10-01T18:00:00')

    subtracted = period.subtract([subtract_1, subtract_2])

    expected_1 = Period.fromIsoFormat(
        '2000-10-01T10:00:00', '2000-10-01T14:00:00')
    expected_2 = Period.fromIsoFormat(
        '2000-10-01T15:00:00', '2000-10-01T17:00:00')
    expected_3 = Period.fromIsoFormat(
        '2000-10-01T18:00:00', '2000-10-01T22:00:00')

    assert len(subtracted) == 3
    assert expected_1 in subtracted
    assert expected_2 in subtracted
    assert expected_3 in subtracted


def test_subtract_4():
    period = Period.fromIsoFormat('2000-10-01T10:00:00', '2000-10-01T22:00:00')

    subtract_1 = Period.fromIsoFormat(
        '2000-10-01T14:00:00', '2000-10-01T15:00:00')

    subtract_2 = Period.fromIsoFormat(
        '2000-10-01T17:00:00', '2000-10-01T18:00:00')

    subtract_3 = Period.fromIsoFormat(
        '2000-10-01T15:00:00', '2000-10-01T19:00:00')

    subtracted = period.subtract([subtract_1, subtract_2, subtract_3])

    expected_1 = Period.fromIsoFormat(
        '2000-10-01T10:00:00', '2000-10-01T14:00:00')
    expected_2 = Period.fromIsoFormat(
        '2000-10-01T19:00:00', '2000-10-01T22:00:00')

    assert len(subtracted) == 2
    assert expected_1 in subtracted
    assert expected_2 in subtracted
