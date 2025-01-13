
def calculate_days_in_month(month: int, year: int) -> int:
    if month in [9, 4, 6, 11]:
        return 30
    elif month == 2:
        if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
            return 29  # leap year
        else:
            return 28
    else:
        return 31

day_of_week = 2  # if Jan 1 1900 is Mon, 1901 is Tues 
count_sundays = 0
year = 1901

while year <= 2000: # better to use variables since tuples are compared elementwise 
    for month in range(1, 13):
        # count condition 
        if day_of_week == 0:
            count_sundays += 1
        # update 
        days_in_month = calculate_days_in_month(month, year)
        day_of_week = (day_of_week + days_in_month) % 7
        
    year += 1

print(count_sundays)