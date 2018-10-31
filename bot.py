from flask import Flask
app = Flask(__name__)

@app.route("/webhook", methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        return 'OK'

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()