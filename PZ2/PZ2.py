import hashlib
from datetime import datetime


class User:
    def __init__(self, username, password, is_active=True):
        self.username = username
        self.password_hash = self.hash_password(password)
        self.is_active = is_active

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password):
        return self.password_hash == hashlib.sha256(password.encode()).hexdigest()





class Administrator(User):
    def __init__(self, username, password, permissions=None):
        super().__init__(username, password)
        self.permissions = permissions if permissions else []

    def add_permission(self, permission):
        self.permissions.append(permission)

class RegularUser(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.last_login = None

    def update_last_login(self):
        self.last_login = datetime.now()

class GuestUser(User):
    def __init__(self):
        super().__init__("guest", "", is_active=False)
        self.limited_access = True



class AccessControl:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.username] = user

    def authenticate_user(self, username, password):
        user = self.users.get(username)
        if user and user.verify_password(password) and user.is_active:
            return user
        return None



if __name__ == "__main__":
    ac = AccessControl()


    admin = Administrator("admin", "adminpass", ["manage_users", "edit_settings"])
    user = RegularUser("john_doe", "mypassword")
    guest = GuestUser()

    ac.add_user(admin)
    ac.add_user(user)
    ac.add_user(guest)

    print("=== СИСТЕМА ВХОДУ ===")
    username = input("Введіть ім’я користувача: ")
    password = input("Введіть пароль: ")

    authenticated_user = ac.authenticate_user(username, password)

    if authenticated_user:
        print(f"\n✅ Вхід виконано: {authenticated_user.username} ({type(authenticated_user).__name__})")

        if isinstance(authenticated_user, Administrator):
            print(f"🔐 Права адміністратора: {authenticated_user.permissions}")

        elif isinstance(authenticated_user, RegularUser):
            authenticated_user.update_last_login()
            print(f"🕓 Останній вхід: {authenticated_user.last_login}")

        elif isinstance(authenticated_user, GuestUser):
            print("👤 Гостьовий доступ (обмежений)")

    else:
        print("\n❌ Невірне ім’я користувача або пароль, або акаунт не активний.")
