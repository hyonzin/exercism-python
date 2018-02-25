from datetime import date

_weekday = {
    "Monday"   : 0,
    "Tuesday"  : 1,
    "Wednesday": 2,
    "Thursday" : 3,
    "Friday"   : 4,
    "Saturday" : 5,
    "Sunday"   : 6,
}

def meetup_day(year, month, day_of_the_week, which):
    day = 1
    week = date(year, month, 1).weekday()
    _week = _weekday[day_of_the_week]

    day += (_week - week)
    if day < 1:
        day += 7
    if day > 7:
        day -= 7

    if which is "teenth":
        while day < 13:
            day += 7
        return date(year, month, day)
    elif which is "last":
        try:
            while True:
                day += 7
                date(year, month, day)
        except Exception as e:
            pass
        return date(year, month, day-7)
    else:
        n_th = ord(which[0]) - ord('0')
        return date(year, month, day+7*(n_th-1))
