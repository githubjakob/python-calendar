from src.main import func
from src.entities.period import Period
from datetime import datetime, timedelta
import time


def test_period():
    start = datetime.fromisoformat('2020-10-01T12:00:00')
    end = datetime.fromisoformat('2020-10-01T13:00:00')
    period = Period(start, end)


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


def test_period_is_overlapping_4():
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
