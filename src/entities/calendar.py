from src.entities.appointment import Appointment
from src.entities.period import Period
from datetime import datetime


class Calendar:
    def __init__(self):
        self.appointments: list = []
        self.opening_time = datetime.fromisoformat('2020-10-01T08:00:00')
        self.closing_time = datetime.fromisoformat('2020-10-01T18:00:00')

    def add_appointment(self, appointment: Appointment):
        self.appointments.append(appointment)

    def get_free_periods(self):
        if len(self.appointments) == 0:
            return [Period(self.opening_time, self.closing_time)]

        if len(self.appointments) == 1:

            period1 = Period(self.opening_time, self.closing_time)
            period2 = self.appointments[0].get_period()

            return period1 - period2
