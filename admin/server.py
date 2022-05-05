from flask import Flask
from threading import Thread

app = Flask("")


@app.route("/")
def root():
    return {"message": "Hello from Mechagodzilla 🤖🦖"}


def run():
    app.run(host="0.0.0.0")


def keep_alive():
    Thread(target=run).start()
