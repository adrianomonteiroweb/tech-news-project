import requests as req
import time


# Requisito 1
def fetch(url):
    try:
        res = req.get(url, timeout=5).raise_for_status()
    except (req.HTTPError, req.ReadTimeout):
        return None

    time.sleep(2)

    return res.text

# https://www.geeksforgeeks.org/response-raise_for_status-python-requests/
# https://realpython.com/python-sleep/


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
