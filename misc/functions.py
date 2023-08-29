from datetime import datetime
import pytz

def current_datetime(timezone : str = 'UTC') -> datetime:
    return datetime.now(tz = pytz.timezone(zone = timezone))