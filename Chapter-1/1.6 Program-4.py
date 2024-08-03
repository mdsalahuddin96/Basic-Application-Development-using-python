from datetime import date
from datetime import timedelta
def tomorrow():
   return date.today()+timedelta(days=1)
print("Today's Date is :",date.today())
print("Tomorrow Date will be :",tomorrow())
