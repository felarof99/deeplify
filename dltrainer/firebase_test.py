#!/usr/bin/env python
import pyrebase

config = {
  "apiKey": "AIzaSyB38Yt-RwENhJdvlkeOxej8LFh80FZPibI",
  "authDomain": "ychack-f2bfb.firebaseapp.com",
  "databaseURL": "https://ychack-f2bfb.firebaseio.com",
  "storageBucket": "ychack-f2bfb.appspot.com"
}


firebase = pyrebase.initialize_app(config)
db = firebase.database()


data = {"name": "Mortimer 'Morty' Smith"}
db.child("users").push(data)


storage = firebase.storage()


import os
os.listdir('.')


storage.child("validate.py").put("./validate.py")


x = storage.child("validate.py").download("validate.py", "validate.py")


x


help(storage.child().download)


apiKey: "AIzaSyB38Yt-RwENhJdvlkeOxej8LFh80FZPibI",
authDomain: "ychack-f2bfb.firebaseapp.com",
databaseURL: "https://ychack-f2bfb.firebaseio.com",
projectId: "ychack-f2bfb",
storageBucket: "ychack-f2bfb.appspot.com",
messagingSenderId: "1053500273864"


# from firebase import firebase
firebase = firebase.FirebaseApplication('https://ychack-f2bfb.firebaseio.com', None)
new_user = 'Ozgur Vatansever'

result = firebase.post('/users', new_user, {'print': 'pretty'}, {'X_FANCY_HEADER': 'VERY FANCY'})
print result

# result = firebase.post('/users', new_user, {'print': 'silent'}, {'X_FANCY_HEADER': 'VERY FANCY'})bb


import firebase


dir(firebase.Firebase)

