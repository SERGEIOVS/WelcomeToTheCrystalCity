import sqlite3,sys

from pathlib import Path

# путь к Scripts/Python
sys.path.append(str(Path(__file__).resolve().parent))


# Словарь таблиц: имя таблицы -> список колонок
tables = {
    "Buildings": ["title", "category", "size"],
    "Vehicles": ["name", "type", "speed"]
}
db_name = input("db_name: ")
# Подключение к базе
conn = sqlite3.connect(db_name)
cursor = conn.cursor()





def create_table():
    global table_name
    table_name = input("table title: ").strip()

    if table_name not in tables:
        cols = input("Введите имена колонок через запятую: ").split(",")
        cols = [c.strip() for c in cols]
        tables[table_name] = cols  # сохраняем колонки
    columns_def = ", ".join(f"{col} TEXT" for col in tables[table_name])
    cursor.execute(f'CREATE TABLE IF NOT EXISTS "{table_name}" ({columns_def})')
    conn.commit()
    print(f"Таблица '{table_name}' создана или уже существует.")


def insert_into_table(values):
    global cur_table_name
    if cur_table_name not in tables:
        print(f"Таблица '{cur_table_name}' не найдена!")
        return
    cols = ", ".join(tables[cur_table_name])
    placeholders = ", ".join("?" for _ in tables[cur_table_name])
    cursor.execute(f'INSERT INTO "{cur_table_name}" ({cols}) VALUES ({placeholders})', values)
    conn.commit()

def show_table():
    global cur_table_name
    if table_name not in tables:
        print(f"Таблица '{table_name}' не найдена!")
        return
    cursor.execute(f'SELECT * FROM "{cur_table_name}"')
    rows = cursor.fetchall()
    if rows:
        for idx, row in enumerate(rows, 1):
            print(f"{idx}. " + " | ".join(f"{col}={val}" for col, val in zip(tables[cur_table_name], row)))
    else:
        print(f"Таблица '{cur_table_name}' пуста!")
        cur_table_name = input("table title: ").strip()

        change_table(curtable_name=cur_table_name)


def change_table():
    global cur_table_name,table_name
    new_table_name = input("table title: ").strip()
    if new_table_name in tables:
        table_name = new_table_name
        print(f"Текущая таблица: {cur_table_name}")

    
    

"""
# === Пример использования ===
create_tables()
insert_into_table(table_name, ("Castle", "Military", "Huge"))
insert_into_table("Vehicles", ("Tank", "Armored", "Slow"))

print("\n--- Buildings ---")
show_table("Buildings")

print("\n--- Vehicles ---")
show_table("Vehicles")


"""

actions = {

    "create"  : create_table,
    "insert"  : insert_into_table,
    "show"    : show_table,
    "change"  : change_table,
    "exit"    : quit
}




run = True
while run:
    action = input("action: ")
    if action in actions:
        actions[action]()


conn.close()
quit()
