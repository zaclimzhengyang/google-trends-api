from _collections_abc import dict_keys
from typing import Any, List, Dict

import requests
import json
from pprint import pprint

from models.trends import Trends, date_string_to_datetime, number_of_shares_string_to_int
from mongo_utils.save_trend_objects import save_trends

response: requests.Response = requests.get("https://trends.google.com/trends/api/dailytrends?hl=en-US&tz=-480&geo=SG&ns=15") # get link under 'Network' tab in Chrome DevTools
response_status: int = response.status_code # return 200 if ok
clean_response: str = response.text[5:] # remove ')]}'\n' from response
clean_response_json: dict[str, Any] = json.loads(clean_response) # convert response to json

print(response_status)
with open("response.json", "w") as f:
    json.dump(clean_response_json, f, indent=4) # save response to json file

# pprint(clean_response_json)

# returns dict_keys(['default'])
clean_response_json_keys: dict_keys = clean_response_json.keys()
# print(clean_response_json_keys)

# returns dict_keys(['trendingSearchesDays', 'endDateForNextRequest', 'rssFeedPageUrl'])
clean_response_json_default_keys: dict_keys = clean_response_json.get("default").keys()
# print(clean_response_json_default_keys)

# returns <class 'list'>
# print(type(clean_response_json.get("default").get("trendingSearchesDays")))

# returns title of the first trend
first_trend_title: str = clean_response_json.get("default").get("trendingSearchesDays")[0].get("trendingSearches")[0].get("title").get("query")
# print(first_trend_title)

# returns dict_keys(['query', 'exploreLink'])
title_keys: dict_keys = clean_response_json.get("default").get("trendingSearchesDays")[0].get("trendingSearches")[0].get("title").keys()
# print(title_keys)

# returns dict_keys(['title', 'formattedTraffic', 'relatedQueries', 'image', 'articles', 'shareUrl'])
trending_searches_keys = clean_response_json.get("default").get("trendingSearchesDays")[0].get("trendingSearches")[0].keys()
# print(trending_searches_keys)

# returns formatted traffic of the first trend
first_trend_formatted_traffic: str = clean_response_json.get("default").get("trendingSearchesDays")[0].get("trendingSearches")[0].get("formattedTraffic")
# pprint(first_trend_formatted_traffic)

# returns list of articles of the first trend
first_trend_searches_article: List[Dict[str, Any]] = clean_response_json.get("default").get("trendingSearchesDays")[0].get("trendingSearches")[0].get("articles")
# pprint(first_trend_searches_article)


trending_searches_by_day: List[Dict[str, Any]] = clean_response_json.get("default").get("trendingSearchesDays")
# pprint(trending_searches_by_day)

list_of_trends: List[Trends] = []

for trending_searches_day_dict in trending_searches_by_day:
    date: str = trending_searches_day_dict.get("date")
    formatted_date: str = trending_searches_day_dict.get("formattedDate")
    trending_searches: List[Dict[str, Any]] = trending_searches_day_dict.get("trendingSearches")
    for trending_search in trending_searches:
        title_dict: Dict[str, str] = trending_search.get("title")
        title: str = title_dict.get("query")
        number_of_shares: str = trending_search.get("formattedTraffic")
        trend_object: Trends = Trends(title=title, date=date_string_to_datetime(formatted_date), number_of_shares=number_of_shares_string_to_int(number_of_shares))
        list_of_trends.append(trend_object)

save_trends(list_of_trends)