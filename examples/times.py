from datetime import datetime, timedelta

t = datetime(2020, 1, 1)
t += timedelta(days=256, hours=-8)
print(t, t.weekday())

t = datetime.now()
t -= timedelta(days=4)
print(t)

c1 = datetime.strptime('10 May 2015 13:54:36.773 -0700', '%d %b %Y %H:%M:%S.%f %z')
c2 = datetime.strptime('10 May 2015 13:54:36.773 -0000', '%d %b %Y %H:%M:%S.%f %z')
print(abs(c2-c1))
print(abs(c1-c2))

import time
s = time.time()
print(s, type(s))
e = time.time()
tme = e - s
print(e)
print(f"{tme:f}")
print(f"Time taken: {tme:.10f} seconds")