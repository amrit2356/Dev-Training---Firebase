import pyrebase
from config import firebaseConfig


firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

#Signup Account

    new_email = input("Enter your email")
    new_password = input('Enter your Password')
    confirm_password = input('Reenter your Password to confirm')
    try:
        if new_password == confirm_password:
            auth.create_user_with_email_and_password(new_email,new_password)
    except:
        print("Passwords not entered properly.")

    else:
        print("Sign in Complete. Welcome to my First App on Firebase :P.")

