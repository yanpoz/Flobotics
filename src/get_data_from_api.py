import requests
from jsonpath_ng import parse


def fetch_json(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch JSON from URL:", url)
        return None
    

def get_data_from_api(url: str, companies):
    json_data = fetch_json(url)
    node = find_node_by_name(json_data, "indexrisersfallersleaders")
    return node
