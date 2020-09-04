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


def test_merge_3():
    period1 = Period.fromIsoFormat(
        '2020-10-01T10:00:00', '2020-10-01T14:00:00')

    period2 = Period.fromIsoFormat(
        '2020-10-01T13:00:00', '2020-10-01T18:00:00')

    merged = merge([period2, period1])

    expected_period = Period.fromIsoFormat(
        '2020-10-01T10:00:00', '2020-10-01T18:00:00')

    assert len(merged) == 1
    assert expected_period in merged


def test_merge_4():
    period1 = Period.fromIsoFormat(
        '2020-10-01T10:00:00', '2020-10-01T14:00:00')

    period2 = Period.fromIsoFormat(
        '2020-10-01T13:00:00', '2020-10-01T18:00:00')

    period3 = Period.fromIsoFormat(
        '2020-10-01T20:00:00', '2020-10-01T21:00:00')

    merged = merge([period2, period3, period1])

    expected_1 = Period.fromIsoFormat(
        '2020-10-01T10:00:00', '2020-10-01T18:00:00')
    expected_2 = Period.fromIsoFormat(
        '2020-10-01T20:00:00', '2020-10-01T21:00:00')

    assert len(merged) == 2
    assert expected_1 in merged
    assert expected_2 in merged


def test_merge_4():
    period1 = Period.fromIsoFormat(
        '2020-10-01T08:00:00', '2020-10-01T12:00:00')

    period2 = Period.fromIsoFormat(
        '2020-10-01T14:00:00', '2020-10-01T15:00:00')

    period3 = Period.fromIsoFormat(
        '2020-10-01T12:00:00', '2020-10-01T18:00:00')

    merged = merge([period2, period3, period1])

    expected_1 = Period.fromIsoFormat(
        '2020-10-01T08:00:00', '2020-10-01T18:00:00')

    assert len(merged) == 1
    assert expected_1 in merged


def test_merge_5():
    period1 = Period.fromIsoFormat(
        '2020-10-01T08:00:00', '2020-10-01T12:00:00')

    period2 = Period.fromIsoFormat(
        '2020-10-01T14:00:00', '2020-10-01T15:00:00')

    period3 = Period.fromIsoFormat(
        '2020-10-01T12:00:00', '2020-10-01T18:00:00')

    period4 = Period.fromIsoFormat(
        '2100-10-01T12:00:00', '2100-10-01T18:00:00')

    merged = merge([period2, period4, period3, period1])

    expected_1 = Period.fromIsoFormat(
        '2020-10-01T08:00:00', '2020-10-01T18:00:00')
    expected_2 = Period.fromIsoFormat(
        '2100-10-01T12:00:00', '2100-10-01T18:00:00')

    assert len(merged) == 2
    assert expected_1 in merged
    assert expected_2 in merged


def test_merge_6():
    period1 = Period.fromIsoFormat(
        '2020-10-01T08:00:00', '2020-10-01T12:00:00')

    period2 = Period.fromIsoFormat(
        '2020-10-01T11:00:00', '2020-10-01T15:00:00')

    period3 = Period.fromIsoFormat(
        '2020-10-01T13:00:00', '2020-10-01T18:00:00')

    merged = merge([period2, period3, period1])

    expected_1 = Period.fromIsoFormat(
        '2020-10-01T08:00:00', '2020-10-01T18:00:00')

    assert len(merged) == 1
    assert expected_1 in merged


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
