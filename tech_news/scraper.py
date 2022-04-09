import requests as req
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        res = req.get(url, timeout=3)
        res.raise_for_status()
    except (req.HTTPError, req.Timeout):
        return None
    else:
        return res.text

# https://www.geeksforgeeks.org/response-raise_for_status-python-requests/
# https://realpython.com/python-sleep/


# Requisito 2
def scrape_novidades(html_content):
    div_selector = "div.tec--card__info h3 a::attr(href)"
    return Selector(html_content).css(div_selector).getall()

# https://github.com/scrapy/parsel


# Requisito 3
def scrape_next_page_link(html_content):
    button_selector = "a.tec--btn::attr(href)"
    return Selector(html_content).css(button_selector).get()


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
