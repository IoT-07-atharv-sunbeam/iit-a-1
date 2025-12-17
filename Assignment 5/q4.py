import datetime

current_datetime = datetime.datetime.now()

print("Current date and time:", current_datetime)

day_of_week_index = current_datetime.weekday()

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print("Day of the week:", days_of_week[day_of_week_index])