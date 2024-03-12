import json
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

with open('usuarios.json', 'r') as file:
    users_data = json.load(file)

secure_users = []
num = 0
for user in users_data:
    num = num + 1
    secure_user = {
        "id": num,
        "nombre": user["id"],
        "password": hash_password(user["password"])
    }
    secure_users.append(secure_user)

with open('secure-users.json', 'w') as file:
    json.dump(secure_users, file, indent=4)