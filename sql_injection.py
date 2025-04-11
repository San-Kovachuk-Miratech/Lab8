import sqlite3
import os

# Уявімо, що user_id приходить ззовні (наприклад, з веб-запиту)
user_id_input = "1 OR 1=1" # Шкідливий ввід

conn = sqlite3.connect(':memory:') # Приклад з базою в пам'яті
cursor = conn.cursor()

# НЕБЕЗПЕЧНО: Пряма конкатенація або форматування рядка
# CodeQL виявить цю вразливість (cs/sql-injection)
query = f"SELECT * FROM users WHERE id = {user_id_input}"
print(f"Executing potentially unsafe query: {query}")

try:
    # У реальному коді тут був би виклик cursor.execute(query)
    # Для демонстрації просто виводимо запит
    pass
except sqlite3.Error as e:
    print(f"An error occurred: {e}")

conn.close()

# Безпечний варіант (для порівняння):
# query_safe = "SELECT * FROM users WHERE id = ?"
# cursor.execute(query_safe, (user_id_input,)) # Використання параметризованого запиту