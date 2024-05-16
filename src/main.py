from csv_parser import get_companies_from_csv
from api_parser import get_stocks_from_api
from printer import print_as_table


def main():
    companies_csv_path = 'input.csv'
    api_url = 'https://api.londonstockexchange.com/api/v1/pages?path=home'
    html_url= 'https://www.londonstockexchange.com/stock/'

    companies = get_companies_from_csv(companies_csv_path)

    stocks = get_stocks_from_api(api_url, companies)
    
    if not stocks: return 1 #TODO

    print_as_table(stocks)












if __name__ == '__main__': 
    main()