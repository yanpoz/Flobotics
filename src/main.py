from csv_io import read_companies_from_csv, save_companies_as_csv
from api_parser import get_stocks_from_api
from html_parser import get_stocks_from_html


def main():
    csv_input_path = 'input.csv'
    csv_api_output_path = 'api_output.csv'
    csv_html_output_path = 'html_output.csv'
    api_url = 'https://api.londonstockexchange.com/api/v1/pages?path=home'
    html_url= 'https://www.londonstockexchange.com'


    companies = read_companies_from_csv(csv_input_path)

    get_stocks_from_api(api_url, companies)
    save_companies_as_csv(csv_api_output_path, companies)

    get_stocks_from_html(html_url, companies)
    save_companies_as_csv(csv_html_output_path, companies)
    return 0












if __name__ == '__main__': 
    main()