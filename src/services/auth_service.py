from src.utils.security import hash_password

def register_new_account(user_data: dict):

    plain_password = user_data.get("password")

    if not plain_password:
        raise ValueError("Password tidak boleh kosong")

    # hashing password
    hashed_password = hash_password(plain_password)

    # ganti password dengan hash
    user_data["password"] = hashed_password

    # contoh simpan ke database
    # auth_repository.create_user(user_data)

    return {
        "username": user_data["username"],
        "email": user_data["email"]
    }