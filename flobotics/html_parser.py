from requests import Response
from requests_html import HTMLSession


def build_url(domain: str, company: dict[str,str]) -> str:
    company_code = company['stock code'].upper()
    company_name = company['company name'].lower().replace(' ', '-')
    url = domain + '/stock/' + company_code + '/' + company_name + '/company-page'
    return url


def get_rendered_page(url: str) -> Response:
    session = HTMLSession()
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    response = session.get(url, headers=headers)
    response.html.render(sleep=1, keep_page=True, scrolldown=1)
    
    return response


def get_stocks_from_html(domain: str, companies: list[dict[str,str]]):
    for company in companies:
        response = get_rendered_page(build_url(domain, company))        

        timestamp = response.html.find('span.refreshed-time', first=True)
        price_tag = response.html.find('span.price-tag', first=True)
        company['timestamp'] = timestamp.full_text
        company['value'] = price_tag.full_text