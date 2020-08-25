import os
import datetime
from django.utils import timezone
from datetime import timedelta


dateandtime = "Aug. 25, 2020, 6:29 a.m."
only_date = datetime.datetime.strptime(dateandtime, "%b. %d, %Y, %M %p.")
print(only_date)
