from src.entities.calendar import Calendar
from src.entities.appointment import Appointment


def test_calendar():
    appointment = Appointment('2020-10-01T08:00:00', '2020-10-01T12:00:00')

    calendar = Calendar()

    calendar.add_appointment(appointment)
