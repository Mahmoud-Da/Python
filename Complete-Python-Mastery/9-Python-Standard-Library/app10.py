# import datetime

# dt = datetime.datetime(2018, 1, 1)

from datetime import datetime
import time

dt = datetime(2018, 1, 1)
print(dt)
# 2018-01-01 00:00:00

dt = datetime.now()
print(dt)
# 2025-03-13 10:02:31.675504

dt = datetime.strptime("2018/01/01", "%Y/%m/%d")
print(dt)
# 2018-01-01 00:00:00

dt = datetime.fromtimestamp(time.time())
print(dt)
# 2025-03-13 11:20:19.657717

print(f"{dt.year}/{dt.month}")
# 2025/3

print(dt.strftime("%Y/%m"))
# 2025/03


dt1 = datetime(2018, 1, 1)
dt2 = datetime.now()
print(dt2 > dt1)
# True
