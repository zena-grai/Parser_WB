from wb_parser_prod import ParserWB
import datetime
from connect import DB

obj_DB = DB()
obj_DB.clear_table()

start = datetime.datetime.now()

# Аккумуляторы для автомобилей +-1500 товаров
url = 'https://catalog.wb.ru/catalog/autoproduct12/v1/catalog?cat=128636&limit=100&sort=popular&page=number_page&xsubject=5819&appType=128&curr=byn&lang=ru&dest=-59208&regions=1,4,22,30,31,33,38,40,48,66,68,69,70,80,83,112,114&spp=0&TestGroup=no_test&TestID=no_test'
obj = ParserWB(url)
obj.main()

# Аккумуляторы для ИБП +-2700
url = 'https://catalog.wb.ru/catalog/electronic17/catalog?TestGroup=control&TestID=331&appType=1&cat=128306&curr=rub&dest=-1257786&page=number_page&regions=80,83,38,4,64,33,68,70,30,40,86,75,69,1,66,110,22,48,31,71,112,114&sort=popular&spp=29&xsubject=2196'
obj = ParserWB(url)
obj.main()

# Элементы питания +-31000 товаров
url = 'https://catalog.wb.ru/catalog/electronic14/catalog?TestGroup=control&TestID=331&appType=1&cat=59132&curr=rub&dest=-1257786&page=number_page&regions=80,83,38,4,64,33,68,70,30,40,86,75,69,1,66,110,22,48,31,71,112,114&sort=popular&spp=29&xsubject=792'
obj = ParserWB(url)
obj.main()

# Аккумуляторы для мотоциклов +-875 товаров
url = 'https://catalog.wb.ru/catalog/autoproduct15/catalog?TestGroup=control&TestID=331&appType=1&cat=128697&curr=rub&dest=-1257786&page=number_page&regions=80,83,38,4,64,33,68,70,30,40,86,75,69,1,66,110,22,48,31,71,112,114&sort=popular&spp=29&xsubject=4129'
obj = ParserWB(url)
obj.main()

# Моторное масло +-60000 товаров
url = 'https://catalog.wb.ru/catalog/autoproduct13/catalog?TestGroup=control&TestID=331&appType=1&curr=rub&dest=-1257786&page=number_page&regions=80,83,38,4,64,33,68,70,30,40,86,75,69,1,66,110,22,48,31,71,112,114&sort=popular&spp=29&subject=3906'
obj = ParserWB(url)
obj.main()

end = datetime.datetime.now()
total = end - start
print(f'Затраченное время: {str(total)}')
