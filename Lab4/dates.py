#1

from datetime import datetime, timedelta
today = datetime.now()
five_days_ago = today - timedelta(days=5)
print(five_days_ago)

#2

from datetime import datetime, timedelta
today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Today is:",today.strftime("%Y.%m.%d"))
print("Yesteray is:",yesterday.strftime("%Y.%m.%d"))
print("Tomorrow is:",tomorrow.strftime("%Y.%m.%d"))

#3

from datetime import datetime, timedelta
today = datetime.now()
print(today.strftime("%Y.%m.%d"))

#4

from datetime import datetime, timedelta
import math
def date_difference_in_seconds(date1, date2):
    date_format = "%Y-%m-%d %H:%M:%S" 
    dt1 = datetime.strptime(date1, date_format)
    dt2 = datetime.strptime(date2, date_format)
    
    time_difference = dt2 - dt1
    seconds_difference = time_difference.total_seconds()
    
    return math.fabs(seconds_difference)
one = input()
two = input()
print(date_difference_in_seconds(one,two))