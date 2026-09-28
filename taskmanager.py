attempts = 0
max_attempts = 3
correct_username = "Elio1k"
correct_password = "Coolguy123"

def menu():
    

print("Welcome to task manager. Please login")


while attempts < max_attempts:
    user_name = input("Enter username: ")
    pwrd = input("Enter password: ") 
    if user_name == correct_username and pwrd == correct_password:
        print("Access granted")
        break
    else:
        attempts += 1 
        remaining_attempts = max_attempts - attempts
        if user_name != "Elio1k":
            print("Wrong username or password")
        elif pwrd != "Coolguy123":
            print("Wrong password")
    if attempts == max_attempts:
        print("Access denied, too many wrong attempts")
