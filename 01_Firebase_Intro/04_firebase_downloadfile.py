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
    
    # Storage
    # Challenge 1: Uploading a File to Storage to Firebase's Storage.
    storage = firebase.storage()
    cloudfilename = input("Enter the filename you want to have in cloud")
    try:
        # Uploading a sample text file on Firebase.
        storage.child(cloudfilename).download("/home/amrit/Documents/Dev Training - Firebase/01_Firebase_Intro/test_files/","file_downloaded.txt")
    except:
        print("Permission Denied...Check the permissions on firebase account")
    else:
        print("File Downloaded...")
