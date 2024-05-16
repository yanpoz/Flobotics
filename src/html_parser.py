def get_stocks_from_html(domain: str, companies: list[dict[str,str]]):
    for company in companies:
    # https://www.londonstockexchange.com/stock/HSBA/hsbc-holdings-plc/company-page
        company_code = company['code'].upper()
        company_name = company['name'].lower().replace(' ', '-')
        url = domain + '/stock/' + company_code + '/' + company_name + '/company-page'
        print(url)


    pass