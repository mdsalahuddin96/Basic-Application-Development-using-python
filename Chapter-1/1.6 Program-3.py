from datetime import date
from datetime import timedelta
def yesterday():
    today=date.today()
    yesterday=today-timedelta(days=1)
    return yesterday
print("Today's Date is :",date.today())
print("yesterday was :",yesterday())
