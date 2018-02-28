import requests
from requests import HTTPError
from bs4 import BeautifulSoup
import logging
import json
from Utils import simple_request

COVERTION_DICT = {"Jan": "01",
                  "Feb": "02",
                  "Mar": "03",
                  "Apr": "04",
                  "May": "05",
                  "Jun": "06",
                  "Jul": "07",
                  "Aug": "08",
                  "Sep": "09",
                  "Oct": "10",
                  "Nov": "11",
                  "Dec": "12"}


def convert_date(original_date):
    arr = original_date.split(",")
    year = arr[-1].strip()
    month_day = arr[0].split(" ")
    month = COVERTION_DICT[month_day[0]] if month_day[0] in COVERTION_DICT else month_day[0]
    day = month_day[1]
    return "{0}-{1}-{2}".format(year, month, day)


def deal_with_result(response):
    res_list = []
    single_res = {}
    if response:
        soup = BeautifulSoup(response, "lxml")
        for link in soup.find_all("article"):
            title_field = link.a
            single_res["title"] = title_field["title"]
            single_res["link"] = title_field["href"]
            single_res["date"] = convert_date(link.div.span.text)
            single_res["content"] = ""
            res_list.append(json.dumps(single_res))
            single_res.clear()

    return res_list


def get_single_page(base_url="http://strategiccoin.com/category/news/page/{0}", page_number=1):
    real_url = base_url.format(page_number)
    return deal_with_result(simple_request(real_url))


if __name__ == '__main__':
    a = 1
    my_url = "http://strategiccoin.com/category/news/"
    res_list = get_single_page(page_number=2)
    for ele in res_list:
        print(ele)