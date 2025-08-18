import hashlib, secrets, hmac

_users = {}  # in-memory store: username -> (salt, hash)

def _hash_pw(pw: str, salt: bytes) -> bytes:
    return hashlib.pbkdf2_hmac("sha256", pw.encode(), salt, 100_000)

def register_user(username: str, password: str) -> bool:
    if username in _users: raise ValueError("Username already exists")
    salt = secrets.token_bytes(16)
    _users[username] = (salt, _hash_pw(password, salt))
    return True

def login_user(username: str, password: str) -> bool:
    rec = _users.get(username)
    if not rec: return False
    salt, stored = rec
    return hmac.compare_digest(_hash_pw(password, salt), stored)

def main():
    while True:
        choice = input("1. Register 2. Login 3. Exit: ")
        if choice == "1":
            u = input("Username: ")
            p = input("Password: ")
            try:
                register_user(u, p)
                print("Registered successfully!")
            except ValueError as e:
                print(e)
        elif choice == "2":
            u = input("Username: ")
            p = input("Password: ")
            if login_user(u, p):
                print("Login successful!")
            else:
                print("Invalid credentials!")
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()