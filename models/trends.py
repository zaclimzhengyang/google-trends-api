from datetime import datetime
from typing import NewType

from pydantic import BaseModel


# TrendsTitle = NewType("TrendsTitle", str)
# NumberOfShares = NewType("NumberOfShares", int)

def date_string_to_datetime(date_string: str) -> datetime:
    """
    Converts a date string "Tuesday, October 18, 2022" to a datetime object
    """
    return datetime.strptime(date_string, "%A, %B %d, %Y")

def number_of_shares_string_to_int(number_of_shares_string: str) -> int:
    """
    Convert a string "1K+" to an int 1000
    """
    str_num: str = ""
    for char in number_of_shares_string:
        if char.isnumeric():
            str_num += char
    int_num = int(str_num)
    return int_num * 1000

class Trends(BaseModel):
    title: str
    date: datetime
    number_of_shares: int
