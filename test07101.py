from datetime import datetime, timedelta

dt = datetime(2015, 7, 10, 12, 20, 10)

dt1 = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')

now = datetime.now()
print now
now = now + timedelta(hours=10)
print now


