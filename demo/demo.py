#!/usr/bin/env python
import pyrebase
import time

config = {
  "apiKey": "AIzaSyB38Yt-RwENhJdvlkeOxej8LFh80FZPibI",
  "authDomain": "ychack-f2bfb.firebaseapp.com",
  "databaseURL": "https://ychack-f2bfb.firebaseio.com",
  "storageBucket": "ychack-f2bfb.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
storage = firebase.storage()

# Push image to firebase storage
# Run the kubernetes pod
# Sleep for a while
# Get result from firebase db and print it


img_file = "12.png"


storage.child("img.png").put(img_file)


from subprocess import call
call('kubectl apply -f ../dltrainer/trainer-deploy.yml', shell=True)



while all_results.each()==None:
    time.sleep(5)
    all_results = db.child("result").get()


for res in all_results.each():
    print(res.key())
    print(res.val())



def stream_handler(message):
    print(message["event"]) # put
    print(message["path"]) # /-K7yGTTEp7O549EzTYtI
    print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}
    print("\n\n")

my_stream = db.child("result").stream(stream_handler, stream_id="new_posts")

