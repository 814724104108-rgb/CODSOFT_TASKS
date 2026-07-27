username = input("Enter Username: ")
password = input("Enter Password: ")

if username == "admin" and password == "admin123":
    print("Login Successful!")
else:
    print("Invalid Username or Password")

with open("log.txt", "a") as file:
    file.write(username + " logged in.\n")