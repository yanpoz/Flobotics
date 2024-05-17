from csv_io import read_companies_from_csv, save_companies_as_csv
from api_parser import get_stocks_from_api
from html_parser import get_stocks_from_html


def main():
    csv_input_path = 'input.csv'
    csv_api_output_path = 'api_output.csv'
    csv_html_output_path = 'html_output.csv'
    api_url = 'https://api.londonstockexchange.com/api/v1/pages?path=home'
    html_url= 'https://www.londonstockexchange.com'


    try:
        companies = read_companies_from_csv(csv_input_path)    

        try: 
            get_stocks_from_api(api_url, companies)
            save_companies_as_csv(csv_api_output_path, companies)
        except Exception as e:
            print(f"Error with API parsing: {e}")

        try:
            get_stocks_from_html(html_url, companies)
            save_companies_as_csv(csv_html_output_path, companies)
        except Exception as e:
            print(f"Error with HTML parsing: {e}")

    except Exception as e:
        print(f"Error with input CSV file: {e}")


if __name__ == '__main__': 
    main()