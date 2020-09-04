from src.entities.appointment import Appointment
from src.entities.period import Period


def test_appointment():
    appointment = Appointment('2020-10-01T08:00:00', '2020-10-01T12:00:00')

    period = appointment.get_period()

    assert period is not None
