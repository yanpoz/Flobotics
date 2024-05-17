from csv_io import get_companies_from_csv, save_companies_as_csv
from api_parser import get_stocks_from_api
from html_parser import get_stocks_from_html


def main():
    companies_csv_input_path = 'input.csv'
    companies_csv_api_output_path = 'api_output.csv'
    companies_csv_html_output_path = 'html_output.csv'
    api_url = 'https://api.londonstockexchange.com/api/v1/pages?path=home'
    html_url= 'https://www.londonstockexchange.com'

    companies = get_companies_from_csv(companies_csv_input_path)

    get_stocks_from_api(api_url, companies)
    save_companies_as_csv(companies_csv_api_output_path, companies)


    # get_stocks_from_html(html_url, companies)
    # save_companies_as_csv(companies_csv_html_output_path, companies)
    return 0












if __name__ == '__main__': 
    main()