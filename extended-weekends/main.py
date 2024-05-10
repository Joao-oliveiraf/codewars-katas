# If the first day of the month is a Friday, it is likely that the month will have an Extended Weekend.
# That is, it could have five Fridays, five Saturdays and five Sundays.
#
# In this Kata, you will be given a start year and an end year. Your task will be to find months that have extended weekends and return:
#
# - The first and last month in the range that has an extended weekend
# - The number of months that have extended weekends in the range, inclusive of start year and end year.
# For example:
#
# solve(2016,2020) = ("Jan","May",5). #The months are: Jan 2016, Jul 2016, Dec 2017, Mar 2019, May 2020

# TODO - Function to check if first day of given month it's a friday - use time lib
# TODO - Append to list -> Used to calculate how many months in interval meet the criteria 1st = friday (len of list)
# TODO - Return Tuple of list[0], list[-1], len(list)

import datetime
from calendar import isleap


def solve(a, b):
    extended_weekend_months = []
    isweekend_day = 0
    for i in range(a, b+1):
        for months in range(1, 13):
            # se o primeiro dia do mes for sexta fazemos a lógica
            if datetime.date(year=i, month=months, day=1).weekday() == 4:
                if months in [1, 3, 5, 7, 8, 10, 12]: # 31 dias
                    for days in range(1, 32):
                        date_to_check = datetime.date(year=i, month=months, day=days)
                        if date_to_check.weekday() in [4, 5, 6]:
                            isweekend_day += 1
                            #extended_weekend_months.append(date_to_check.ctime())
                    if isweekend_day == 15:
                        extended_weekend_months.append(datetime.date(year=i, month=months, day=1).strftime("%b"))
                        isweekend_day = 0
                    else:
                        isweekend_day = 0
                elif months in [4, 6, 9, 11]:
                    for days in range(1, 31): # 30 dias
                        date_to_check = datetime.date(year=i, month=months, day=days)
                        if date_to_check.weekday() in [4, 5, 6]:
                            isweekend_day += 1
                            # extended_weekend_months.append(date_to_check.ctime())
                    if isweekend_day == 15:
                        extended_weekend_months.append(datetime.date(year=i, month=months, day=1).strftime("%b"))
                        isweekend_day = 0
                    else:
                        isweekend_day = 0
                elif months == 2 and isleap(i):
                    for days in range(1, 30): # fev com 29 dias
                        date_to_check = datetime.date(year=i, month=months, day=days)
                        if date_to_check.weekday() in [4, 5, 6]:
                            isweekend_day += 1
                    if isweekend_day == 15:
                        extended_weekend_months.append(datetime.date(year=i, month=months, day=1).strftime("%b"))
                        isweekend_day = 0
                    else:
                        isweekend_day = 0
                elif months == 2 and not isleap(i): # fev com 28 dias
                    for days in range(1, 29):
                        date_to_check = datetime.date(year=i, month=months, day=days)
                        if date_to_check.weekday() in [4, 5, 6]:
                            isweekend_day += 1
                    if isweekend_day == 15:
                        extended_weekend_months.append(datetime.date(year=i, month=months, day=1).strftime("%b"))
                        isweekend_day = 0
                    else:
                        isweekend_day = 0

    rt_tp = tuple([extended_weekend_months[0], extended_weekend_months[-1], len(extended_weekend_months)])
    return rt_tp




if __name__ == '__main__':
    print(solve(1800, 2500))
