from cryptography.fernet import Fernet
def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()



'''def key_generator():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

key = load_key()
fer = Fernet(key)

def view():
    with open('password.txt', "r") as file:
        for line in file:
            text = line.rstrip()
            user, pwd = text.split("|")
            print("User: " + user + "\nPassword: " + fer.decrypt(pwd.encode()).decode())

def enter():
    user = input("Enter Username: ")
    password = input("Enter Password: ")

    with open('password.txt', "a") as f:
        f.write(user + " | " + fer.encrypt(password.encode()).decode())
        f.write("\n")


while True:
    req = input("Would you like to enter another password or view the list? ")

    if req == "view":
        view()
    elif req == "enter":
        enter()
    elif req == "exit":
        break
    else:
        print("Invalid input")
        continue