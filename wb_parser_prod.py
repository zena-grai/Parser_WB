import datetime
import os
import time
from tqdm import tqdm
import requests
import json
import pandas as pd
import fake_useragent
from connect import DB

user = fake_useragent.UserAgent().random


class ParserWB:
    def __init__(self, url):
        self.url = url
        self.headers = {
            'Accept': '*/*',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Origin': 'https://www.wildberries.ru',
            'Referer': 'https://www.wildberries.ru/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': user,
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
        }

    def get_category(self, i):
        response = requests.get(self.url.replace('number_page', str(i)), headers=self.headers)
        print(f'Статус - {response.status_code}. Страница - {i}.')
        return response.json()

    def prepare_items(self, response):
        obj_DB = DB()
        obj_DB.make_connection()
        obj_DB.clear_table()
        products_row = response.get('data', {}).get('products', None)

        if products_row is not None and len(products_row) > 0:
            for product in tqdm(products_row):
                url_card = f"https://www.wildberries.ru/catalog/{str(product['id'])}/detail.aspx"

                ref_card, seller_card = self.get_url_for_data(str(product['id']))
                item_data, item_seller = self.get_card_data(ref_card, seller_card)

                obj_DB.add_product(url_card, product, item_data, item_seller)


    def get_url_for_data(self, card_id):
        if len(card_id) == 8:
            ref_card = f"https://basket-number_rep.wb.ru/vol{card_id[:3]}/part{card_id[:5]}/{card_id}/info/ru/card.json"
            ref_seller = f"https://basket-number_rep.wb.ru/vol{card_id[:3]}/part{card_id[:5]}/{card_id}/info/sellers.json"
        elif len(card_id) == 9:
            ref_card = f"https://basket-number_rep.wb.ru/vol{card_id[:4]}/part{card_id[:6]}/{card_id}/info/ru/card.json"
            ref_seller = f"https://basket-number_rep.wb.ru/vol{card_id[:4]}/part{card_id[:6]}/{card_id}/info/sellers.json"
        else:
            print("Артикул не соответствует заданной длине!")

        for i in range(1, 13):
            new_ref_card = ref_card.replace('number_rep', str(i).zfill(2))
            new_ref_card_seller = ref_seller.replace('number_rep', str(i).zfill(2))
            if requests.get(new_ref_card).status_code == 200:
                return new_ref_card, new_ref_card_seller

    def get_card_data(self, card_url, seller_url):
        try:
            card_u = requests.get(card_url).json()["grouped_options"]
            seller_u = requests.get(seller_url).json()
            return card_u, seller_u
        except:
            print('Something went wrong...')

    def main(self):
        i = 1
        while True:
            response = self.get_category(i)
            if response.get('data', {}).get('products', []) == []:
                break
            self.prepare_items(response)
            i += 1
        print('---Success---')



if __name__ == '__main__':
    url = 'https://catalog.wb.ru/catalog/autoproduct12/v1/catalog?cat=128636&limit=100&sort=popular&page=number_page&xsubject=5819&appType=128&curr=byn&lang=ru&dest=-59208&regions=1,4,22,30,31,33,38,40,48,66,68,69,70,80,83,112,114&spp=0&TestGroup=no_test&TestID=no_test'
    obj = ParserWB(url)
    obj.main()
