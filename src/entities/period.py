from datetime import datetime, timedelta
import time


def sort_by_start(list_of_periods):
    if len(list_of_periods) == 0:
        return []

    if len(list_of_periods) == 1:
        return list_of_periods

    list_of_periods.sort(key=lambda period: period.start)

    return list_of_periods


def merge(list_of_periods):
    """
    Adds up all the periods from the input list that are overlapping
    Examples:
    - merge([]) _> []
    - merge([P(1,5)]) -> [P(1,5)]
    - merge([P(1,4), P(2,5)]) -> [P(1,5)]
    - merge([P(1,4), P(2,5), P(7,8)]) -> [P(1,5), P(7,8)]
    """

    if len(list_of_periods) == 0:
        return []

    if len(list_of_periods) <= 2:
        return list_of_periods

    sorted_periods = sort_by_start(list_of_periods)

    result = []
    temp = sorted_periods[0]

    for i in range(1, len(sorted_periods)):

        current = sorted_periods[i]

        if temp.is_overlapped(current):
            temp = temp + current
            temp = temp[0]  # we know len == 1 since both are overlapping
        else:
            result.append(temp)
            temp = current

        if i == len(sorted_periods) - 1:
            result.append(temp)

    return result


class Period:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"Period('{self.start}', '{self.end}')"


    @classmethod
    def fromIsoFormat(cls, start, end):
        start_datetime = datetime.fromisoformat(start)
        end_datetime = datetime.fromisoformat(end)
        return Period(start_datetime, end_datetime)

    def get_duration(self):
        return self.end - self.start

    def is_overlapped(self, other):
        if max(self.start, other.start) <= min(self.end, other.end):
            return True
        else:
            return False

    def contains(self, other):
        if not self.is_overlapped(other):
            return False
        else:
            return self.start <= other.start and self.end >= other.end

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

    def __sub__(self, other):
        if self.contains(other):
            first = Period(self.start, other.start)
            second = Period(other.end, self.end)
            return [first, second]
        elif other.contains(self):
            return []
        elif self.is_overlapped(other):
            if self.start < other.start:
                return [Period(self.start, min(self.end, other.start))]
            else:
                return [Period(max(self.start, other.end), self.end)]
        else:
            return [self]

    def subtract(self, others: list):
        if len(others) == 0:
            return [self]

        if len(others) == 1:
            return self - others[0]

        results = [self]

        for i in range(len(others)):
            current = others[i]

            temp = []

            for result in results:
                temp = temp + (result - current)

            results = temp

        return results

    def __repr__(self):
        return 'Period[{0} - {1}]'.format(self.start, self.end)

    def __eq__(self, other) -> bool:
        return self.start == other.start and self.end == other.end
