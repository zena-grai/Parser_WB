from wb_parser_prod import ParserWB

url = f'https://www.wildberries.ru/catalog/avtotovary/zapchasti-na-legkovye-avtomobili/elektrooborudovanie?sort=popular&page=1&xsubject=5819'
obj = ParserWB(url)
obj.main()

url = f'https://www.wildberries.ru/catalog/elektronika/ofisnaya-tehnika/ibp-i-aksessuary?sort=popular&page=1&xsubject=2196'
obj = ParserWB(url)
obj.main()

url = f'https://www.wildberries.ru/catalog/elektronika/kabeli-i-zaryadnye-ustroystva?sort=popular&page=1&xsubject=792'
obj = ParserWB(url)
obj.main()

url = f'https://www.wildberries.ru/catalog/avtotovary/mototovary/elektrooborudovanie?sort=popular&page=1&xsubject=4129'
obj = ParserWB(url)
obj.main()

url = f'https://www.wildberries.ru/catalog/avtotovary/masla-i-zhidkosti/motornye-masla'
obj = ParserWB(url)
obj.main()

