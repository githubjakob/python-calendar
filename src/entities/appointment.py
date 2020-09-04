from src.entities.period import Period
from datetime import datetime


class Appointment:
    def __init__(self, start: str, end: str):
        start_datetime = datetime.fromisoformat(start)
        end_datetime = datetime.fromisoformat(end)
        self.period = Period(start_datetime, end_datetime)

    def get_period(self):
        return self.period
