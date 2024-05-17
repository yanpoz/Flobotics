from datetime import datetime
import requests
from pytz import timezone


def fetch_json(url) -> dict:
    response = requests.get(url)
    if response.status_code != 200:
        raise requests.ConnectionError
    return response.json() 


def find_node_by_value(data: dict, key: str, value: str) -> dict[str, str]|None:
    if isinstance(data, dict):
        if data.get(key) == value:
            return data
        for item in data.values():
            result = find_node_by_value(item, key, value)
            if result is not None:
                return result
            
    if isinstance(data, list):
        for item in data:
            result = find_node_by_value(item, key, value)
            if result is not None:
                return result
            
    return None


def get_stocks_from_api(url: str, companies: list[dict[str,str]]):
    json_data = fetch_json(url)
    all_stocks = find_node_by_value(json_data, 'name', 'ftseindextickers')
    if not all_stocks: return None  #TODO

    time_zone = timezone('Europe/London')
    for company in companies:
        stock = find_node_by_value(all_stocks, 'tidm', company['stock code'])
        if not stock: continue #TODO

        localized_time = datetime.now().astimezone(time_zone).strftime("%y.%m.%d %H:%M:%S %Z")
        company['timestamp'] = localized_time
        company['value'] = stock['lastprice']
