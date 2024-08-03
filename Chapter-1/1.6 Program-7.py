import datetime
t=datetime.time(12,46,30)
print("Time is :",t)
d=datetime.date.today()
print("Date is  :",d)
dt=datetime.datetime.combine(d,t)
print("Date & Time is:",dt)
