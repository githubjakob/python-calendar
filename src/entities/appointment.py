from src.entities.period import Period


class Appointment:
    def __init__(self, start: str, end: str):
        self.period = Period(start, end)
