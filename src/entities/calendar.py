from src.entities.appointment import Appointment
from src.entities.period import Period
from src.entities.duration import Duration
from datetime import datetime, date
from enum import Enum


class Dictlist(dict):
    def __setitem__(self, key, value):
        try:
            self[key]
        except KeyError:
            super(Dictlist, self).__setitem__(key, [])
        self[key].append(value)


weekdays = {'MONDAY': 0, 'TUESDAY': 1, 'WEDNESDAY': 2,
            'THURSDAY': 3, 'FRIDAY': 4, 'SATURDAY': 5, 'SUNDAY': 6}


class Calendar:
    def __init__(self):
        self.appointments: list = []
        self.open_periods = Dictlist()
        self.opening_time = datetime.fromisoformat('2020-10-01T08:00:00')
        self.closing_time = datetime.fromisoformat('2020-10-01T18:00:00')

    def set_opening_times(self, weekday, opening_time, closing_time):
        self.open_periods[weekdays[weekday]] = Duration(
            opening_time, closing_time)

    def get_opening_times(self, weekday):
        return self.open_periods[weekdays[weekday]]

    def add_appointment(self, appointment: Appointment):
        self.appointments.append(appointment)

    def get_free_periods(self):
        total_time = Period(self.opening_time, self.closing_time)

        all_blocked_periods = list(
            map(lambda a: a.get_period(), self.appointments))

        return total_time.subtract(all_blocked_periods)

    def get_free_periods_for_date(self, date):

        weekday = date.weekday()

        opening_times = self.open_periods[weekday]

        # todo extend for multiple opening periods
        opening_time = opening_times[0]

        open = datetime.combine(date, opening_time.start)
        close = datetime.combine(date, opening_time.end)

        total_time = Period(open, close)

        print(total_time)

        all_blocked_periods = list(
            map(lambda a: a.get_period(), self.appointments))

        return total_time.subtract(all_blocked_periods)
