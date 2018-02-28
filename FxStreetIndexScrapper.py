from Utils import simple_request
from bs4 import BeautifulSoup
import json


def get_sigle_page(query, page):
    real_url = f"https://www.fxstreet.com/search?q={query}&hPP=25&idx=FxsIndexPro&p={page}&is_v=1"
    print(real_url)
    resp = simple_request(real_url)
    return deal_with_response(resp)


def deal_with_response(resp):
    res_list = []
    single_res = {}
    if resp:
        soup = BeautifulSoup(resp, "lxml")
        print(soup.prettify())
        for link in soup.find_all("article"):
            print(link)

    return res_list

if __name__ == '__main__':
    get_sigle_page("cryptocurrency", 1)