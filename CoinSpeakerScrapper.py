from bs4 import BeautifulSoup
from datetime import datetime
from dateutil import parser
from UKInvestingScrapper import site_pattern
from Utils import request_with_headers
import json

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36"
}


def deal_with_request(resp):
    if resp:
        soup = BeautifulSoup(resp.text, "lxml")
        for titles in soup.find_all("div", attrs={"class": "sectionContent"}):
            for news_title in titles.find_all("div", attrs={"class": "newsTitle"}):
                for title in news_title.find_all("h3"):
                    yield (title.text, title.a["href"])


def request_index_page(base_url="https://www.coinspeaker.com/category/news/cryptocurrencies/page/{0}",
                       page_number=1):
    real_url = base_url.format(page_number)
    resp = request_with_headers(real_url, headers)
    json_dict = {}
    results = []
    for ele in deal_with_request(resp):
        title, link = ele
        json_dict["title"] = title
        json_dict["link"] = link
        json_dict["date"] = ""
        json_dict["content"] = ""
        results.append(json.dumps(json_dict))

    return results


if __name__ == '__main__':
    date = "February 28 2018 1:23PM"
    datetime_object = datetime.strptime(date, '%B %d %Y %I:%M%p')
    res = request_index_page(page_number=1)
    for ele in res:
        print(ele)