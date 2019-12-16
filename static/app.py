# from flask_cors import CORS
# from flask import Flask, render_template, request
# import requests
# # from folium_maps import return_map
# import os
# from mongoclient import get_geojson


# template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# template_dir = os.path.join(template_dir,'flask','templates')
#
#
#
# coords = (-97,30)
#
# app = Flask(__name__)#,template_folder="/home/app/flask_app/templates/")
#
# CORS(app)
# # coords = get_geojson(coords)
#
#
# @app.route('/')
# def index():
#     print(os.path.dirname(__name__))
#     return render_template('index.html')
#
# @app.route('/leaflet')
# def leaflet():
#     coords = (-97,30)
#     map = return_map(coords)
#
#     return map.get_root().render()
#
# if __name__ == '__main__':
#     app.run(debug=True, host='127.0.0.1', port=8000)
