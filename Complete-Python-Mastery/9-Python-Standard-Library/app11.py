from datetime import datetime, timedelta

dt1 = datetime(2018, 1, 1)
dt2 = datetime.now()

duration = dt2 - dt1
print(duration)
# 2628 days, 11:38:36.052896

print("days", duration.days)
# days 2628

print("seconds", duration.seconds)
# seconds 41970

print("total_seconds", duration.total_seconds())
# total_seconds 227101230.113785


dt1 = datetime(2018, 1, 1) + timedelta(1)
print(dt1)
# 2018-01-02 00:00:00

dt1 = datetime(2018, 1, 1) + timedelta(days=1, seconds=1000)
print(dt1)
# 2018-01-02 00:16:40
