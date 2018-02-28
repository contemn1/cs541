from Utils import simple_request
from bs4 import BeautifulSoup


def deal_with_content_page(response):
    a = 1
    res_list = []
    if response:
        soup = BeautifulSoup(response, "lxml")
        for link in soup.find_all("div", attrs={"class": "article__body"}):
            res_list.append(link.text.strip())

    return res_list

if __name__ == '__main__':
    url = "http://strategiccoin.com/bitcoin-friendly-startup-revolut-adding-8000-users-day/"
    res = simple_request(url)
    deal_with_content_page(res)