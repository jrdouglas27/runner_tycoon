# Utils

def day_of_week(day_num):
    
    weekday_num = day_num % 7
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[weekday_num]

