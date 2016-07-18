from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Wayne! I have gotten this far, now what? :-) I am running Flask, yay!'





if __name__ == '__main__':
    app.run()
