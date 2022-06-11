import csv
from errno import EACCES
from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.telia.lt/prekes/mobilieji-telefonai?filter=brand:samsung').text
soup = BeautifulSoup(source, 'html.parser')

block = soup.find_all('div', class_ = 'mobiles-product-card card card__product card--anim js-product-compare-product')

with open("Telia telefonai.csv", "w", encoding="UTF-8", newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Phone Model', 'Monthly Price', 'Price'])

    for each_block in block:
        try:
            name = each_block.find("a", class_ = "mobiles-product-card__title js-open-product").text.strip()
            monthly_price = each_block.find("div", class_ = "mobiles-product-card__price-marker").text.strip()
            price = each_block.find("div", class_ = "mobiles-product-card__full-price price").find("div", class_ = "mobiles-product-card__price-marker").text.strip()
            csv_writer.writerow([name, monthly_price, price])
        except:
            pass
