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


def scrap(selector, context):
    return context.css(selector).get()


def scrap_all(selector, context):
    return context.css(selector).getall()


# Requisito 4
def scrape_noticia(html_content):
    context = Selector(html_content)

    obj = {}

    obj["url"] = scrap('head link[rel="canonical"]::attr(href)', context)
    obj["title"] = scrap(".tec--article__header__title::text", context)
    obj["timestamp"] = scrap("#js-article-date::attr(datetime)", context)

    writer = scrap(".z--font-bold *::text", context)
    obj["writer"] = writer.strip() if writer else None

    raw_shares = scrap(".tec--toolbar__item::text", context)
    if (raw_shares):
        obj["shares_count"] = int(raw_shares.split(" ")[1])
    else:
        obj["shares_count"] = 0

    raw_comments_count = scrap("#js-comments-btn::attr(data-count)", context)
    if (raw_comments_count):
        obj["comments_count"] = int(raw_comments_count)
    else:
        obj["comments_count"] = 0

    summary = scrap_all(
        "div.tec--article__body > p:nth-child(1) *::text",
        context
    )
    obj["summary"] = "".join(summary)

    raw_sources = scrap_all(".z--mb-16 div a::text", context)
    obj["sources"] = [source.strip() for source in raw_sources]

    raw_categories = scrap_all("#js-categories a::text", context)
    obj["categories"] = [category.strip() for category in raw_categories]

    return obj


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
