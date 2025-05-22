import hashlib

# 5. Аутентифікація користувачів
users = {
    "kriss": {"password": hashlib.md5("password123".encode()).hexdigest(), "name": "Крістіна Романівна Семенчук"},
    "maki": {"password": hashlib.md5("qwerty".encode()).hexdigest(), "name": "Максим Ігорович Коваленко"},
    "kekeke": {"password": hashlib.md5("adminadmin".encode()).hexdigest(), "name": "Кирило Сергійович Степаненко"}
}

def authenticate():
    login = input("Введіть логін: ")
    if login in users:
        password = input("Введіть пароль: ")
        hashed = hashlib.md5(password.encode()).hexdigest()
        if users[login]["password"] == hashed:
            return f"Ласкаво просимо, {users[login]['name']}!"
        else:
            return "Невірний пароль."
    else:
        return "Користувача не знайдено."

def demo_authentication():
    print(authenticate())

if __name__ == "__main__":
    demo_authentication()
