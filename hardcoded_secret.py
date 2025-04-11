# НЕБЕЗПЕЧНО: Зберігання секретів прямо в коді
# CodeQL може виявити це як потенційну проблему (може залежати від конфігурації правил)
API_KEY = "sk_live_THIS_IS_A_VERY_BAD_IDEA_12345abcde"
DATABASE_PASSWORD = "Password123!"

print(f"Using API Key: {API_KEY[:10]}...") # Навіть якщо не виводити повністю, ключ у коді
print(f"Using Password: {'*' * len(DATABASE_PASSWORD)}")

# Безпечний варіант:
# Зберігати секрети в змінних середовища, конфігураційних файлах поза репозиторієм
# або використовувати системи управління секретами (Vault, AWS Secrets Manager тощо).
# import os
# api_key_safe = os.environ.get("MY_API_KEY")
# db_password_safe = os.environ.get("DB_PASS")