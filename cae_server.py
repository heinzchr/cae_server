import sys, os.path
#import the base classes
#from models.rolls import base_roll
from flask import Flask, request

#sys.setrecursionlimit(2000)

tmp_directory="./tmp/"


#tmp_base_roll = base_roll()

app = Flask(__name__, static_url_path="")

#entry point for the application with the threejs view
@app.route('/')
def root():
    return app.send_static_file("index.html")

if __name__ == "__main__":
  app.run(
    host="127.0.0.1",
    port=int("5000"),
    debug=True
	)
