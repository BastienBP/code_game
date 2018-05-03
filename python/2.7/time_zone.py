from pytz import all_timezones
from pytz import timezone
from datetime import datetime
import re

str_ = "2018-02-22 09:38:45 America/Los_Angeles"
time_zone_str = (re.findall('[A-Za-z].*', str_ ))
new_str = re.sub('[A-Za-z].*', '', str_)
new_str = new_str.rstrip()
date = datetime.strptime(new_str, "%Y-%m-%d %H:%M:%S")
date_tz = timezone(time_zone_str[0]).localize(date)
print date_tz.strftime("%Y-%m-%d %H:%M:%S %Z%z")
