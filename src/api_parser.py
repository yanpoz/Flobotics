import requests
from jsonpath_ng import parse


def fetch_json(url) -> dict:
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch JSON from URL:", url)
        return {'error': 'err'} #TODO


def find_node_by_value(data, key, value):
    if isinstance(data, dict):
        # Check if the current dictionary has the "name" field
        if data.get(key) == value:
            return data
        # Recursively search nested dictionaries
        for item in data.values():
            result = find_node_by_value(item, key, value)
            if result is not None:
                return result
            
    if isinstance(data, list):
        # Recursively search elements in a list
        for item in data:
            result = find_node_by_value(item, key, value)
            if result is not None:
                return result
            
    return None


def get_data_from_api(url: str, companies):
    json_data = fetch_json(url)
    stock_list = find_node_by_value(json_data, 'name', 'indexrisersfallersleaders')
    # indexrisersfallersleaders = json_data['components'][2]['content'][1]

    return 'no'
