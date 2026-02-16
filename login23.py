def login(username, password):
    if username == "admin" and password == "password123":
        return "Login Successful!"
    return "Access Denied"

if __name__ == "__main__":
    print(login("admin", "password123"))