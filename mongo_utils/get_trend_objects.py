from typing import List, Dict, Any

from models.trends import Trends
from mongo_utils.save_trend_objects import trends_client


def get_all_trends() -> List[Trends]:
    all_trends: List[Trends] = [Trends.parse_obj(trend) for trend in trends_client.find()]
    return all_trends