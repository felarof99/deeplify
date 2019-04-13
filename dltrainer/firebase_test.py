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


storage = firebase.storage()


import os
os.listdir('.')


storage.child("validate.py").put("./validate_original.py")


storage.child("img.png").put("./img.png")

