from Utils import simple_request
from bs4 import BeautifulSoup
import json
import requests

def get_sigle_page(query, page):
    real_url = f"https://www.fxstreet.com"
    resp = requests.post(real_url, data={"indexName": "FxsIndexPro",
                                                   })
    return deal_with_response(resp)


def deal_with_response(resp):
    res_list = []
    single_res = {}
    if resp:
        soup = BeautifulSoup(resp, "lxml")
        for link in soup.find_all("article"):
            print(link)

    return res_list

if __name__ == '__main__':
    paras_map = {"query": "bitcoin",
                 "hitsPerPage": 25,
                 "maxValuesPerFacet": 10,
                 "page": 2,
                 "filters": "CultureName:en",
                 "facets": ["Category", "Tags", "AuthorName"],
                 "tagFilters": ""}
    requests_map = {"indexName": "FxsIndexPro",
                    "params": paras_map}

    print(json.dumps(requests_map))