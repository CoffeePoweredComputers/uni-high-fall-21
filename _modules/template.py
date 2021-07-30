import datetime
import sys
import time

START_WEEK = 31 + int(sys.argv[1])

TEMPLATE = """---
navtitle: Week {} -
n: "{}"
---

{}
: **Lab**{{: .label .label-purp}}

{}
: **Lecture**{{: .label .label-light-blue}}
: **Reading/Post-Reading**{{: .label .label-orange}}
    : **Assigned**{{: .label .label-green}}
: **Homework**{{: .label .label-grey}}
    : **Assigned**{{: .label .label-green}}
: **Challenge Questions**{{: .label .label-dark-blue}}
    : **Assigned**{{: .label .label-green}}


{}
: **Reading/Post-Reading**{{: .label .label-orange}}
    : **Due**{{: .label .label-red}}
: **Homework**{{: .label .label-grey}}
    : **Due**{{: .label .label-red}}


{}
: **Lecture**{{: .label .label-light-blue}}
: **Reading/Post-Reading**{{: .label .label-orange}}
    : **Assigned**{{: .label .label-green}}
: **Homework**{{: .label .label-grey}}
    : **Assigned**{{: .label .label-green}}

{}
: **Reading/Post-Reading**{{: .label .label-orange}}
    : **Due**{{: .label .label-red}}
: **Homework**{{: .label .label-grey}}
    : **Due**{{: .label .label-red}}

{}
: **Nothing Due**

{}
: **Challenge Questions**{{: .label .label-dark-blue}}
    : **Due**{{: .label .label-red}}
"""

startdate = time.asctime(time.strptime('2021 %d 0' % START_WEEK, '%Y %W %w'))
startdate = datetime.datetime.strptime(startdate, '%a %b %d %H:%M:%S %Y')

days = [(startdate + datetime.timedelta(days=i)).strftime("%b %d") for i in range(1, 8)]

print(TEMPLATE.format(sys.argv[1], chr(ord("a") + int(sys.argv[1])), *days))
