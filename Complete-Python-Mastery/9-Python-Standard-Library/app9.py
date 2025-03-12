import time

print(time.time())
# 1741823482.881205


def send_emails():

    for i in range(10000):
        pass


start = time.time()
send_emails()
end = time.time()

duration = end - start
print(duration)
# 0.00016498565673828125
