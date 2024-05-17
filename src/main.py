from csv_io import get_companies_from_csv, save_companies_as_csv
from api_parser import get_stocks_from_api
from html_parser import get_stocks_from_html
from printer import print_as_table


def main():
    companies_csv_input_path = 'input.csv'
    companies_csv_output_path = 'api_output.csv'
    api_url = 'https://api.londonstockexchange.com/api/v1/pages?path=home'
    html_url= 'https://www.londonstockexchange.com'

    companies = get_companies_from_csv(companies_csv_input_path)

    # stocks = get_stocks_from_api(api_url, companies)
    # if not stocks: return 1 #TODO
    # print_as_table(stocks)
    # save_companies_as_csv(companies_csv_output_path, companies)




    stocks = get_stocks_from_html(html_url, companies)
    return 0












if __name__ == '__main__': 
    main()