import sqlite3 as sl


def make_connection():
    try:
        # пытаемся подключиться к базе данных
        con = sl.connect('my-test.db')
        with con:
            con.execute("""
                CREATE TABLE USER (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    age INTEGER
                );
            """)
    except:
        # в случае сбоя подключения будет выведено сообщение в STDOUT
        print('Can`t establish connection to database')

print(make_connection())