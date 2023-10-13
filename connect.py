import sqlite3 as sl

class DB:
    def __init__(self, products):
        self.products = products

    def make_connection(self):
        # пытаемся подключиться к базе данных
        try:
            return sl.connect('my-test.db')
        except:
            # в случае сбоя подключения будет выведено сообщение
            print('Can`t establish connection to database')

    def add_product(self):
        """Добавляем нашу номенклатуру в базу данных"""
        c = self.make_connection()
        # Создаем курсор - это специальный объект который делает запросы и получает их результаты
        cursor = c.cursor()
        # ТУТ БУДЕТ НАШ КОД РАБОТЫ С БАЗОЙ ДАННЫХ
        cursor.execute(f"insert into Products ( values ({self.products['name']}, {self.products['brand']}') ")
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