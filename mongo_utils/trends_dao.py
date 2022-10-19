from typing import List, Dict, Any

import pymongo

from models.trends import Trends


class TrendsDAO:
    """
    Data Access Object to get a Trends from mongo, and save Trends to mongo
    """
    def __init__(self, client: pymongo.MongoClient):
        self.client = client
        self.database = self.client.sgag
        self.trends_client = self.database.trends

    def save_many(self, trends: List[Trends]) -> None:
        trends_dict: List[Dict[str, Any]] = [trend.dict() for trend in trends]
        self.trends_client.insert_many(trends_dict)

    def get_trends(self) -> List[Trends]:
        all_trends: List[Trends] = [Trends.parse_obj(trend) for trend in self.trends_client.find()]
        return all_trends
