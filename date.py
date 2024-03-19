from datetime import date, datetime

def calc_date():
    today = date.today()
    return today.strftime("%B %d, %Y")

def calc_datetime():
    current_time = datetime.now()
    return current_time.strftime("%H hours %M minutes %S seconds")

