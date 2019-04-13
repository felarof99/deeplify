#!/usr/bin/env python
img_file = "bison.png"


run_demo()




def stream_handler(message):
    # print(message["event"]) # put
    # print(message["path"]) # /-K7yGTTEp7O549EzTYtI
    print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}
    print("\n")

my_stream = db.child("result").stream(stream_handler, stream_id="new_posts")


def run_demo():
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
    
    storage.child("img.png").put(img_file)
    from subprocess import call
    call('kubectl apply -f ../dltrainer/trainer-deploy.yml', shell=True)

