def merge(list_of_periods):

    if len(list_of_periods) == 0:
        return []

    if len(list_of_periods) == 1:
        return list_of_periods

    return []


def sort_by_start(list_of_periods):
    if len(list_of_periods) == 0:
        return []

    if len(list_of_periods) == 1:
        return list_of_periods

    list_of_periods.sort(key=lambda period: period.start)

    return list_of_periods
