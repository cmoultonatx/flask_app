from flask_cors import CORS
from flask import Flask, render_template
from folium_maps import return_map

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')
    # return "HELLO WORLD!!! My name is.....CHRIS"

@app.route('/leaflet')
def leaflet():
    
    map = return_map()
    return map

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)
