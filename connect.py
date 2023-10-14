import sqlite3 as sl

class DB:
    def __init__(self):
        pass

    def make_connection(self):
        # пытаемся подключиться к базе данных
        try:
            return sl.connect('my-test.db')
        except:
            # в случае сбоя подключения будет выведено сообщение
            print('Can`t establish connection to database')

    def add_product(self, url, products, item_data, item_seller):
        """Добавляем нашу номенклатуру в базу данных"""
        c = self.make_connection()
        # Создаем курсор - это специальный объект который делает запросы и получает их результаты
        cursor = c.cursor()
        # ТУТ БУДЕТ НАШ КОД РАБОТЫ С БАЗОЙ ДАННЫХ
        sqlite_insert_with_param = """insert into Products (Articyl, Name, Brand, Price, DiscountPrice,Trademark, 
        BatteryСapacity, StartingСurrent, Polarity, ItemHeight, ItemWidth, ItemDepth, BatteryType, Voltage, Volume_L,
        TypeOfEngineOil, Class_Viscosity, Url_product) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?); """

        data_tuple = (products['id'],
                      products['name'],
                      products['brand'],
                      float(products['priceU']) / 100,
                      float(products['salePriceU']) / 100,
                      item_seller['trademark'],
                      next((option["value"] for item in item_data for option in item["options"] if
                            "Емкость" in option["name"]), None),
                      1,
                      next((option["value"] for item in item_data for option in item["options"] if
                            "Полярность" in option["name"]), None),
                      next((option["value"] for item in item_data for option in item["options"] if
                            "Высота предмета" in option["name"]), None),
                      next((option["value"] for item in item_data for option in item["options"] if
                            "Глубина предмета" in option["name"]), None),
                      next((option["value"] for item in item_data for option in item["options"] if
                            "Тип аккумулятора" in option["name"]), None),
                      next((option["value"] for item in item_data for option in item["options"] if
                            "Напряжение" in option["name"]), None),
                      next((option["value"] for item in item_data for option in item["options"] if
                            "Объем (л)" in option["name"]), None),
                      next((option["value"] for item in item_data for option in item["options"] if
                            "Тип моторного масла" in option["name"]), None),
                      next((option["value"] for item in item_data for option in item["options"] if
                            "Класс вязкости" in option["name"]), None),
                      url)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        # КОД ДАЛЬНЕЙШИХ ПРИМЕРОВ ВСТАВЛЯТЬ В ЭТО МЕСТО
        c.commit()
        # Не забываем закрыть соединение с базой данных
        c.close()

"""
if __name__ == '__main__':
    obj = DB()
    obj.make_connection()
    obj.add_product()
"""