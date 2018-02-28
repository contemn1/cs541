import requests
from requests import HTTPError
import logging


def simple_request(url: str) -> str:
    try:
        response = requests.get(url)

    except HTTPError as err1:
        logging.error("Failed to connect to website {0}".format(err1))
        return ''

    return response.text
