from src.entities.calendar import Calendar
from src.entities.appointment import Appointment
from src.entities.period import Period
from src.entities.duration import Duration
from datetime import date


def test_calendar():
    appointment = Appointment('2020-10-01T08:00:00', '2020-10-01T12:00:00')

    calendar = Calendar()

    calendar.add_appointment(appointment)


def test_calendar_get_free_periods():

    calendar = Calendar()

    free_periods = calendar.get_free_periods()

    assert len(free_periods) == 1


def test_calendar_set_opening_times():

    calendar = Calendar()
    calendar.set_opening_times('MONDAY', '10:00:00', '12:00:00')

    open_monday = calendar.get_opening_times('MONDAY')

    assert len(open_monday) == 1
    assert Duration('10:00:00', '12:00:00') in open_monday


def test_calendar_get_free_periods_2():
    appointment = Appointment('2020-10-01T10:00:00', '2020-10-01T12:00:00')

    calendar = Calendar()
    calendar.add_appointment(appointment)

    free_periods = calendar.get_free_periods()

    assert len(free_periods) == 2
    assert Period.fromIsoFormat(
        '2020-10-01T08:00:00', '2020-10-01T10:00:00') in free_periods
    assert Period.fromIsoFormat(
        '2020-10-01T12:00:00', '2020-10-01T18:00:00') in free_periods


def test_calendar_get_free_periods_2():
    appointment1 = Appointment('2020-10-01T10:00:00', '2020-10-01T12:00:00')
    appointment2 = Appointment('2020-10-01T14:00:00', '2020-10-01T15:00:00')

    calendar = Calendar()
    calendar.add_appointment(appointment1)
    calendar.add_appointment(appointment2)

    free_periods = calendar.get_free_periods()

    assert len(free_periods) == 3
    assert Period.fromIsoFormat(
        '2020-10-01T08:00:00', '2020-10-01T10:00:00') in free_periods
    assert Period.fromIsoFormat(
        '2020-10-01T12:00:00', '2020-10-01T14:00:00') in free_periods
    assert Period.fromIsoFormat(
        '2020-10-01T15:00:00', '2020-10-01T18:00:00') in free_periods


def test_calendar_get_free_periods_3():
    appointment1 = Appointment(
        start='2020-10-01T10:00:00', end='2020-10-01T12:00:00')
    appointment2 = Appointment(
        start='2020-10-01T14:00:00', end='2020-10-01T15:00:00')
    appointment3 = Appointment(
        start='2020-10-01T14:00:00', end='2020-10-01T18:00:00')

    calendar = Calendar()
    calendar.add_appointment(appointment1)
    calendar.add_appointment(appointment2)
    calendar.add_appointment(appointment3)

    free_periods = calendar.get_free_periods()

    assert len(free_periods) == 2
    assert Period.fromIsoFormat(
        '2020-10-01T08:00:00', '2020-10-01T10:00:00') in free_periods
    assert Period.fromIsoFormat(
        '2020-10-01T12:00:00', '2020-10-01T14:00:00') in free_periods


def test_calendar_get_free_periods_for_date():
    calendar = Calendar()

    calendar.set_opening_times('THURSDAY', '08:00:00', '18:00:00')

    target_date = date.fromisoformat('2020-10-01')

    free_periods = calendar.get_free_periods_for_date(target_date)

    assert len(free_periods) == 1
    assert Period.fromIsoFormat(
        '2020-10-01T08:00:00', '2020-10-01T18:00:00') in free_periods


def test_calendar_get_free_periods_for_date_2():
    calendar = Calendar()

    appointment1 = Appointment(
        start='2020-10-01T10:00:00', end='2020-10-01T12:00:00')
    calendar.add_appointment(appointment1)

    calendar.set_opening_times('THURSDAY', '08:00:00', '18:00:00')

    target_date = date.fromisoformat('2020-10-01')

    free_periods = calendar.get_free_periods_for_date(target_date)

    assert len(free_periods) == 2
    assert Period.fromIsoFormat(
        '2020-10-01T08:00:00', '2020-10-01T10:00:00') in free_periods
    assert Period.fromIsoFormat(
        '2020-10-01T12:00:00', '2020-10-01T18:00:00') in free_periods
