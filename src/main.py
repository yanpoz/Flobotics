from .get_companies_from_csv import get_companies_from_csv
from .get_data_from_api import get_data_from_api


def main():
    companies = get_companies_from_csv("input.csv")

    for item in companies:
        print(f"Company Name: {item['name']}, Stock Code: {item['code']}")

    get_data_from_api



if __name__ == '__main__': 
    main()