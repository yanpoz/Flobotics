import requests

def get_data_from_api(url: str):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON data
        data = response.json()
        
        # Access the data using dictionary-like syntax
        print(data["key"])  # Replace "key" with the actual key in the JSON
    else:
        print("Error: Could not retrieve data")