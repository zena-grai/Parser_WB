import datetime

import requests
import json
import pandas as pd
#from retry import retry
# pip install openpyxl
import fake_useragent
from bs4 import BeautifulSoup
#from selenium import webdriver


user = fake_useragent.UserAgent().random

class ParserWB:
    def __init__(self, url):
        self.url = url

    def get_category(self, i):

        headers = {
            'Accept': '*/*',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Origin': 'https://www.wildberries.by',
            'Referer': 'https://www.wildberries.by/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': user,
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
        }

        response = requests.get(self.url.replace('number_page', str(i)))

        #print(response.status_code)
        #print(response.json())

        return response.json()

    def prepare_items(self, response, products):
        products_row = response.get('data', {}).get('products', None)
        #print(products_row)
        if products_row is not None and len(products_row) > 0:
            for number_product, product in enumerate(products_row, start=1):
                page_url = self.get_url_for_data(str(product['id']))
                #print(page_url)
                #item_data, item_seller = self.get_card_data(page_url)

                products.append({
                    'number': number_product,
                    'brand': product.get('brand', None),
                    'name': product.get('name', None),
                    'sale': product.get('sale', None),
                    'priceU': float(product.get('priceU')) / 100 if product.get('priceU', None) != None else None,
                    'salePriceU': float(product.get('salePriceU')) / 100 if product.get('salePriceU',
                                                                                        None) is not None else None,
                })
            #print(len(products))
        return products

    def get_url_for_data(self, card_id):
        if len(card_id) == 8:
            ref_card = f"https://basket-number_rep.wb.ru/vol{card_id[:3]}/part{card_id[:5]}/{card_id}/info/ru/card.json"
        elif len(card_id) == 9:
            ref_card = f"https://basket-number_rep.wb.ru/vol{card_id[:4]}/part{card_id[:6]}/{card_id}/info/ru/card.json"
        else:
            print("Артикул не соответствует заданой длине!!!")

        for i in range(1, 13):
            new_ref = ref_card.replace('number_rep', str(i).zfill(2))
            #print(new_ref)
            if requests.get(new_ref).status_code == 200:
                print(new_ref)
                return new_ref

    def get_card_data(self, card_url):
        return requests.get(f'{card_url}/info/ru/card.json').json()["grouped_options"], requests.get(f'{card_url}/info/sellers.json').json()

    def main(self):
        i = 1
        products = []
        while True:
            response = self.get_category(i)
            if response.get('data', {}).get('products', []) == []:
                break
            products = self.prepare_items(response, products)
            i += 1

        self.save_excel(products)

    def save_excel(self, data):
        """сохранение результата в excel файл"""
        pd.DataFrame(data).to_csv('test_products.xls', index=False)
        print(f'Все сохранено в test_products.xls\n')




if __name__ == '__main__':
    url = f'https://catalog.wb.ru/catalog/autoproduct12/v1/catalog?cat=128636&limit=100&sort=popular&page=number_page&xsubject=5819&appType=128&curr=byn&lang=ru&dest=-59208&regions=1,4,22,30,31,33,38,40,48,66,68,69,70,80,83,112,114&spp=0&TestGroup=no_test&TestID=no_test'
    obj = ParserWB(url)
    obj.main()
