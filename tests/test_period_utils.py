from src.utils.period_utils import merge, sort_by_start
from src.entities.period import Period
from datetime import datetime, timedelta


def test_merge_1():

    merged = merge([])

    assert len(merged) == 0


def test_merge_2():
    start1 = datetime.fromisoformat('2020-10-01T10:00:00')
    end1 = datetime.fromisoformat('2020-10-01T14:00:00')
    period1 = Period(start1, end1)

    merged = merge([period1])

    assert len(merged) == 1
    assert period1 in merged


def test_sort_1():
    sorted_periods = sort_by_start([])

    assert len(sorted_periods) == 0


def test_sort_1():
    start1 = datetime.fromisoformat('2020-10-01T10:00:00')
    end1 = datetime.fromisoformat('2020-10-01T14:00:00')
    period1 = Period(start1, end1)

    sorted_periods = sort_by_start([period1])

    assert len(sorted_periods) == 1


def test_sort_2():
    start1 = datetime.fromisoformat('2000-10-01T10:00:00')
    end1 = datetime.fromisoformat('2000-10-01T14:00:00')
    period1 = Period(start1, end1)

    start2 = datetime.fromisoformat('2020-10-01T10:00:00')
    end2 = datetime.fromisoformat('2020-10-01T14:00:00')
    period2 = Period(start2, end2)

    sorted_periods = sort_by_start([period2, period1])

    assert len(sorted_periods) == 2
    assert sorted_periods[0] == period1
    assert sorted_periods[1] == period2
