import sqlite3

# Создание (или подключение к существующей) базы данных
conn = sqlite3.connect('Database.db')
cursor = conn.cursor()
DB_title = input("Database title: ")



# Создание таблицы пользователей
def create_table():
    tables_num = int(input("Tables num: "))
    table_name = input("Table title:    ").strip()

    if not table_name.isidentifier():
        print("Неверное имя таблицы")
    for i in range(tables_num):
        
        cursor.execute(f"""
                            CREATE TABLE IF NOT EXISTS {table_name}(

            column1 TEXT NOT NULL,
            column2 TEXT
            
            );
                       """
                       )
        
        cursor.execute(f"INSERT INTO {table_name} (column1,column2) VALUES (?, ?)", ("player1", "player1@example.com"))

        conn.commit()

# Добавление пользователей
#cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", ("player1", "player1@example.com"))
#cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", ("player2", "player2@example.com"))

# Сохранение изменений

# Вывод всех пользователей
def show_table():
    table_name = input("Table title:    ")

    cursor.execute(f'SELECT * FROM "{table_name}"')
    for row in cursor.fetchall():
        print(row)



run = True
while run:
    querry = input("querry:")
    if querry == "show table": show_table()
    if querry == "create table": create_table()


# Закрытие соединения
conn.close()