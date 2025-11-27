from datetime import datetime, timedelta

t = datetime(2020, 1, 1)
t += timedelta(days=256, hours=-8)
print(t, t.weekday())

t = datetime.now()
t -= timedelta(days=4)
print(t)


import time
s = time.time()
print(s, type(s))
e = time.time()
tme = e - s
print(e)
print(f"{tme:f}")
print(f"Time taken: {tme:.10f} seconds")