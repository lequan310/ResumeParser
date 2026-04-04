from datetime import datetime

from dateutil import parser
from dateutil.relativedelta import relativedelta


def get_position_duration(start: str, end: str) -> dict:
    """Get the duration between two dates.

    Args:
        start (str): start date
        end (str): end date

    Returns:
        dict: duration in years and months
    """
    try:
        start_date = parser.parse(start)
    except ValueError:
        start_date = datetime.now()

    try:
        end_date = parser.parse(end)
    except ValueError:
        end_date = datetime.now()
    finally:
        duration = relativedelta(end_date, start_date)
        return {"year": duration.years, "month": duration.months}
