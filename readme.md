# Задание на внешний сбор данных

Этап 1: Написать класс по работе с парсингом внешних данных
Получить на вход страницу в виде:

https://www.ozon.ru/product/kapsulnaya-kofemashina-krups-piccolo-xs-krasnyy-178842724/?sh=yr-vOjksrA

https://www.wildberries.ru/catalog/18256273/detail.aspx?targetUrl=MI

https://market.yandex.ru/offer/gXBC9f3VsTCE8tua_dKwkA?cpa=1&onstock=1

Сделать парсинг вводимой страницы

Этап 2: Матчинг
Получить из БД мастер товар

К мастеру товару добавить матчинг (добавление товара из ссылки и введение всех данных)

Этап 3: Интеллектуальный поиск

Получить из БД товар

Найти этот товар на площадках

Найти по нему параметры

Внести в БД
## Способ запуска
2. Выполнить следующие команды:
```
cd yandex
pip install -r requirements.txt
scrapy crawl YandexMarketSpider
```
3. Данные сохранятся в файле yandex.json
