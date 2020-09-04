from datetime import datetime, timedelta
import time


class Period:
    def __init__(self, start: datetime, end: datetime):
        self.start = start
        self.end = end

    def get_duration(self) -> timedelta:
        return self.end - self.start

    def is_overlapped(self, other: 'Period') -> bool:
        if max(self.start, other.start) <= min(self.end, other.end):
            return True
        else:
            return False

    def get_overlapped_period(self, other: 'Period') -> 'Period':
        if not self.is_overlapped(other):
            return

        if other.start >= self.start:
            if self.end >= other.end:
                return Period(other.start, other.end)
            else:
                return Period(other.start, self.end)
        elif other.start < self.start:
            if other.end >= self.end:
                return Period(self.start, self.end)
            else:
                return Period(self.start, other.end)

    def __add__(self, other):
        if self.is_overlapped(other):
            earliest_start = min(self.start, other.start)
            latest_end = max(self.end, other.end)
            period = Period(earliest_start, latest_end)
            return [period]
        else:
            return [self, other]

    def __radd__(self, other):
        return self.__add__(other)

    def __repr__(self):
        return 'Period[{0} - {1}]'.format(self.start, self.end)

    def __eq__(self, other) -> bool:
        return self.start == other.start and self.end == other.end
