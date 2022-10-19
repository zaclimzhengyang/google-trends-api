from typing import Dict, Any, List

import pymongo
from flask import Flask

from models.trends import Trends
from mongo_utils.get_trend_objects import get_all_trends
from mongo_utils.trends_dao import TrendsDAO

app = Flask(__name__)

client: pymongo.MongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
trends_dao: TrendsDAO = TrendsDAO(client)


@app.route("/get_trends", methods=["GET"])
def get_trends() -> List[Dict[str, Any]]:
    all_trends: List[Trends] = trends_dao.get_trends()
    all_trends.sort(key=lambda trend: trend.number_of_shares, reverse=True)
    return [trend.dict() for trend in all_trends[:7]]


if __name__ == "__main__":
    app.run(port=5000)