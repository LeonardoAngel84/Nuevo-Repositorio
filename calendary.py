import calendar
from datetime import datetime

yy = datetime.now().year

for i in range(1,13):
    print(calendar.month(yy,i))