import datetime
import sys
import time

START_WEEK = 31 + int(sys.argv[1])

TEMPLATE = """---
navtitle: Week {} -
n: "{}"
---

{}
: **Lab**{{: .label .label-purp}} [](#)

{}
: **Lecture**{{: .label .label-light-blue}} X.1
: **zyBooks**{{: .label .label-orange}} [Topic X.2 - Participation](#), [Topic X - Challenge](#)
    : **Assigned**{{: .label .label-green}}
: **PrairieLearn**{{: .label .label-dark-blue}} [Homework X.1](#), [Post-reading X.2](#)
    : **Assigned**{{: .label .label-green}}


{}
: **zyBooks**{{: .label .label-orange}} [Topic X.2 - Participation](#)
    : **Due**{{: .label .label-red}}
: **PrairieLearn**{{: .label .label-dark-blue}} [Homework X.1](#), [Post-reading X.2](#)
    : **Due**{{: .label .label-red}}


{}
: **Lecture**{{: .label .label-light-blue}} X.2
: **zyBooks**{{: .label .label-orange}} [Topic X.1 - Participation](#)
    : **Assigned**{{: .label .label-green}}
: **PrairieLearn**{{: .label .label-dark-blue}} [Homework X.2](#), [Post-reading X.1](#)
    : **Assigned**{{: .label .label-green}}

{}
: **zyBooks**{{: .label .label-orange}} [Topic X.1 - Participation](#)
    : **Due**{{: .label .label-red}}
: **PrairieLearn**{{: .label .label-dark-blue}} [Homework X.2](#), [Post-reading X.1](#)
    : **Due**{{: .label .label-red}}

{}
: **Nothing Due**

{}
: **zyBooks**{{: .label .label-orange}} [Topic X - Challenge Activities](#)
    : **Due**{{: .label .label-red}}
"""

startdate = time.asctime(time.strptime('2021 %d 0' % START_WEEK, '%Y %W %w'))
startdate = datetime.datetime.strptime(startdate, '%a %b %d %H:%M:%S %Y')

days = [(startdate + datetime.timedelta(days=i)).strftime("%b %d") for i in range(1, 8)]

print(TEMPLATE.format(sys.argv[1], chr(ord("a") + int(sys.argv[1])), *days))
