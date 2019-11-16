from flask import Flask
app=Flask(__name__)

@app.route("/")
def hello():
    print("test")
    return "Hi"