from datetime import date,datetime

def current_date():
    return str(date.today());

def get_nextdate():
    return str(date.today()+ date.timedelta(days=1));


def current_month_dates():
    current = datetime.today()
    start = current.replace(day=1)
    return (start.date(),current.date())
