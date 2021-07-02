import datetime
import sys
import time

START_WEEK = 31 + int(sys.argv[1])

TEMPLATE = """
---
navtitle: Week {} -
---

{}

{}

{}

{}

{}

{}

{}
"""

startdate = time.asctime(time.strptime('2021 %d 0' % START_WEEK, '%Y %W %w'))
startdate = datetime.datetime.strptime(startdate, '%a %b %d %H:%M:%S %Y')

days = [(startdate + datetime.timedelta(days=i)).strftime("%b %d") for i in range(1, 8)]

print(TEMPLATE.format(sys.argv[1], *days))
