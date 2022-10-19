from typing import List, Dict, Any

import pymongo

from models.trends import Trends

# Client to connect to a database
client: pymongo.MongoClient = pymongo.MongoClient("mongodb://localhost:27017/")

# Get database
database: pymongo.database.Database = client.sgag

# Get collection
trends_client: pymongo.collection.Collection = database.trends


def save_trends(trends: List[Trends]) -> None:
    trends_dict: List[Dict[str, Any]] = [trend.dict() for trend in trends]
    trends_client.insert_many(trends_dict)