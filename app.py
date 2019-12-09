from flask_cors import CORS
from flask import Flask

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "HELLO WORLD!!! My name is.....CHRIS"

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)
