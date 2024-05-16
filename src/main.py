from csv_parser  import get_column_from_csv
from api_parser  import get_stocks_from_api
from html_parser import get_stocks_from_html
from printer import print_as_table


def main():
    companies_csv_path = 'input.csv'
    api_url = 'https://api.londonstockexchange.com/api/v1/pages?path=home'
    html_url= 'https://www.londonstockexchange.com/stock/'

    company_codes = get_column_from_csv(companies_csv_path, 'stock code')

    # stocks = get_stocks_from_api(api_url, company_codes)    
    # if not stocks: return 1 #TODO
    # print_as_table(stocks)

    stocks = get_stocks_from_html(html_url, company_codes)

    return 0












if __name__ == '__main__': 
    main()