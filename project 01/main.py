from sys import exit
users =[]

# user sign up function
def signUp():
    print('Create your account in abc bank ')
    name = str(input('Enter your name: '))
    email = str(input("enter your email:"))
    password = str(input("enter your password:"))
    user = {
        'name': name,
        'email': email,
        'password': password
    }
    # check user in users if user already exist then print a error message otherwise create a user 
    for i in users:
        if i['email'] == user['email']:
            print("Email already exist")
            signUp()
    users.append(user)

    print('Account created successfully')

    print("==== Select your options ======= ")
    print('=================================')
    print("1. Main Menu")
    print("2. Login")
    print("3. Exit")
    option = int(input("Enter a number: "))
    if option == 1: 
        welcome()
    elif option == 2:
        login()
    elif option == 3:
        myExit()
    else:
        print("Invalid option")
        welcome()


# user login function
def login():
    print("this is login function")

# withdraw balance function 
def withdraw():
    pass

# deposit balance function
def deposit():
    pass

# check balance function
def checkBalance():
    pass

#exit function 
def myExit():
    print('Exiting...')
    exit()
# welcome function 
def welcome():
    print('===== welcome to  ABC bank ===== ')
    print('================================')
    print("==== Select your options ======= ")
    print('=================================')
    print("1. Sign up")
    print("2. Login")
    print("3. Exit")
    option = int(input("Enter a number: "))
    if option == 1:
        signUp()
    elif option == 2:
        login()
    elif option == 3:
        myExit()
    else:
        print("Invalid option")
        welcome()


welcome()