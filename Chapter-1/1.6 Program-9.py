import datetime
min6=datetime.timezone(datetime.timedelta(hours=-6))
plus6=datetime.timezone(datetime.timedelta(hours=6))
d=datetime.datetime.now(min6)
print(min6,':',d)
print(datetime.timezone.utc,':',d.astimezone(datetime.timezone.utc))
print(plus6,':',d.astimezone(plus6))
d_system=d.astimezone()
print("Bangladesh Standard Time:",d_system.tzinfo,':',d_system)
