from src.entities.calendar import Calendar
from src.entities.appointment import Appointment
from src.entities.period import Period


def test_calendar():
    appointment = Appointment('2020-10-01T08:00:00', '2020-10-01T12:00:00')

    calendar = Calendar()

    calendar.add_appointment(appointment)


def test_calendar_get_free_periods():

    calendar = Calendar()

    free_periods = calendar.get_free_periods()

    assert len(free_periods) == 1


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
    appointment1 = Appointment('2020-10-01T10:00:00', '2020-10-01T12:00:00')
    appointment2 = Appointment('2020-10-01T14:00:00', '2020-10-01T15:00:00')
    appointment3 = Appointment('2020-10-01T14:00:00', '2020-10-01T18:00:00')

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
