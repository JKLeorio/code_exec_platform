from datetime import datetime, timezone


def get_current_time_utc():
    return datetime.now(timezone.utc)