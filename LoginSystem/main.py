import hashlib
import re
import csv 
import sys 

# password hashing 
def hash_password(password):
    hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest()
    return hashed_password


# print(hash_password("password9999955"))


# password validation 
def password_validation(password):
    patterns = re.compile("(?=(.*[a-z]){2,})(?=(.*[A-Z]){1,})(?=(.*[0-9]){1,})")
    special_characters = """
                "!@#$%^&*()-+?_=,<>/`\/.}]{["]}'
    """   
    if len(password) >= 8 and len(password) <=12 and patterns.match(password):
        for char in password:
            if char in special_characters:
                return True 
    return False

# password_validation("Password@1")




# read file

def read_file():
    db = open("./password.txt", 'r')

    user_lst = []
    password_lst = []
    for d in db:
        u, p = d.split(",")
        p = p.strip()
        user_lst.append(u)
        password_lst.append(p)
    data = dict(zip(user_lst, password_lst))
    return data


# print(read_file())



# register user 
def register(username, password1, password2):
    db = read_file()

    if username in db:
        print("User already exists!")
    else:
        if password1 == password2:
            if password_validation(password1):
                password = hash_password(password1) 
                db = open("./password.txt", "a", newline='')
                db.write(f"{username},{password}\n")
                print("User registered successfully!")
            else:
                print("""
                    Password length must be between 8 to 12 characters.
                    Password must have 1 capital letter.
                    Password needs to have 1 digit and 1 speial character
                """)

        else:
            print("Password doesn't match. Try again")


# register("sidd", 'Password.1', 'Password.1')


# login user 
def login(username, password):
    db = read_file()
    if username in db:
        if hash_password(password) == db[username]:
            print(f"Welcome, {username}. You are logged in.")
        else:
            print("Incorrect password. Please try again!")
    else:
        print("No such user. Please register.")

# login('sidd', 'Password.1')




# change password

# command line interface 
# python main.py register u p1 p2
if __name__== "__main__":
    args = sys.argv[1:]
    if args:
        function_name = args[0]
        if function_name == register.__name__:
            if not len(args)  == 4:
                print("register username password1 password2")
            else:
                u = args[1]
                p1 = args[2]
                p2 = args[3]
                register(u, p1, p2)
        if function_name == login.__name__:
            if not len(args) == 3:
                print("login username password")
            else:
                u = args[1]
                p = args[2]
                login(u, p)
    else:
        print("Please call the correct function with arugments")
            