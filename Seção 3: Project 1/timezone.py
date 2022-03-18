from datetime import datetime
import pytz


class Timezone:

    def return_utc_now():
        dt = datetime.utcnow()
    
        return dt.strftime("%Y-%m-%d %H:%M:%S")

    def datetime_preferred(dt, timezone):

        date_time_obj = datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')
        tz = pytz.timezone(timezone)
        return pytz.utc.localize(date_time_obj).astimezone(tz)