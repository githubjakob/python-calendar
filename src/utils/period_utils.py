import functools
from src.entities.period import Period
from typing import List


def merge(list_of_periods: List[Period]) -> list:
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

    if len(list_of_periods) == 1:
        return list_of_periods

    if len(list_of_periods) == 2:
        return list_of_periods[0] + list_of_periods[1]

    sorted_periods: List[Period] = sort_by_start(list_of_periods)

    result = []
    temp: Period = sorted_periods[0]

    for i in range(1, len(sorted_periods)):

        current: Period = sorted_periods[i]

        if temp.is_overlapped(current):
            temp = temp + current
            temp = temp[0]  # we know len == 1 since both are overlapping
        else:
            result.append(temp)
            temp = current

        if i == len(sorted_periods) - 1:
            result.append(temp)

    return result


def sort_by_start(list_of_periods):
    if len(list_of_periods) == 0:
        return []

    if len(list_of_periods) == 1:
        return list_of_periods

    list_of_periods.sort(key=lambda period: period.start)

    return list_of_periods
