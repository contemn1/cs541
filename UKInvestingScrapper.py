from Utils import request_with_headers
from Utils import simple_request
from bs4 import BeautifulSoup
import re
import json

site_pattern = re.compile("^https?://")
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36"
}


def deal_with_request(resp):
    if resp:
        soup = BeautifulSoup(resp, "lxml")
        for titles in soup.find_all("div", attrs={"class": "largeTitle"}):
            for title in titles.find_all("a", attrs={"class": "title"}):
                if title["href"] and site_pattern.search(title["href"]):
                    yield (title["title"], title["href"])


def request_index_page(base_url="https://uk.investing.com/news/cryptocurrency-news/{0}",
                        page_number=1):
    real_url = base_url.format(page_number)
    resp = request_with_headers(real_url, headers)
    json_dict = {}
    results = []
    for ele in deal_with_request(resp.text):
        title, link = ele
        json_dict["title"] = title
        json_dict["link"] = link
        json_dict["date"] = ""
        json_dict["content"] = ""
        results.append(json.dumps(json_dict))

    return results


if __name__ == '__main__':
    url = "https://uk.investing.com/news/cryptocurrency-news/2"
    res = request_index_page(page_number=2)
    for ele in res:
        print(ele)