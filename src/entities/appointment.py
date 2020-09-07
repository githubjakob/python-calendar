from src.entities.period import Period
from datetime import datetime


class Appointment:
    def __init__(self, start, end):
        self.period = Period.fromIsoFormat(start, end)

    def get_period(self):
        return self.period
