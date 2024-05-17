from requests_html import HTMLSession


def build_urls(domain: str, companies: list[dict[str,str]]):
    for company in companies:
        company_code = company['stock code'].upper()
        company_name = company['company name'].lower().replace(' ', '-')
        url = domain + '/stock/' + company_code + '/' + company_name + '/company-page'
        yield url


def get_stocks_from_html(domain: str, companies: list[dict[str,str]]):
    for url in build_urls(domain, companies):
        session = HTMLSession()

        # Send GET request and render JavaScript
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        response = session.get(url, headers=headers)
        response.html.render(sleep=1, keep_page=True, scrolldown=1)

        with open("scraped_data.html", "w", encoding="utf-8") as f:
            f.write(response.html.html)



        # Extract titles using CSS selector
        ticker_symbol = response.html.find('span.price-tag', first=True)
        price_tag = response.html.find('span.price-tag', first=True)
        print(ticker_symbol, price_tag)

    pass