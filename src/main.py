from src.csv_parser import get_companies_from_csv
from src.api_parser import get_data_from_api


def main():
    companies_csv_path = 'input.csv'
    data_api_url = 'https://api.londonstockexchange.com/api/v1/pages?path=home'


    companies = get_companies_from_csv(companies_csv_path)

    for item in companies:
        print(f"Company Name: {item['name']}, Stock Code: {item['code']}")
    
    res = get_data_from_api(data_api_url, companies)
    print(res)












if __name__ == '__main__': 
    main()