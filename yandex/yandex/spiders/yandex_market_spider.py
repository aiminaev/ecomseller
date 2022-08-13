import scrapy
import os
import selectorlib

API_KEY = 'd1dcdf62bba47b325add21a0679230da'


class YandexDescriptionHeadingFormatter(selectorlib.Formatter):
    def format(self, text: str):
        return text.replace(':', '').strip()


class YandexMarketSpider(scrapy.Spider):
    name = 'YandexMarketSpider'
    allowed_domains = ['market.yandex.ru']
    url_link = "https://market.yandex.ru/offer/gXBC9f3VsTCE8tua_dKwkA"
    start_urls = ['http://api.scraperapi.com/?api_key=' + API_KEY + '&url=' + url_link + '&render=true']
    formatters = selectorlib.Formatter.get_all()
    product_page_extractor = selectorlib.Extractor.from_yaml_file(
        os.path.join(os.path.dirname(__file__), './yandex_market_selector.yml'), formatters=formatters)

    def parse(self, response):
        print("procesing:" + response.url)

        data = self.product_page_extractor.extract(response.text)

        if data:
            data['product_link'] = self.url_link
            yield data
