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
storage.child("validate.py").download("validate.py", "validate.py")

import validate
validate.run_validate()