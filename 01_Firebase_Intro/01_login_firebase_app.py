import pyrebase
from config import firebaseConfig


firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Authentication
# Login
try:
    email = input("Enter Your Email ")
    password = input("Enter Your Password ")
    auth.sign_in_with_email_and_password(email,password)

except:
    print("Invalid Email or Password.")

else:
    print("Successfully Signed In")
