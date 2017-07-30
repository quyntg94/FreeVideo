from flask import Flask
from flask_restful import Resource, Api, reqparse
import json
import codecs
import os


APP_ROOT = os.path.dirname(os.path.abspath(__file__))
COOK_PATH = os.path.join(APP_ROOT, "cook.json")
MUSIC_PATH = os.path.join(APP_ROOT, "music.json")
VLOG_PATH = os.path.join(APP_ROOT, "vlog.json")
COMEDY_PATH = os.path.join(APP_ROOT, "comedy.json")

app = Flask(__name__)
api = Api(app)

class CookListRes(Resource):
    def get(self):
        with codecs.open(COOK_PATH, 'r', 'utf-8-sig') as data_file:
            return json.load(data_file)

class MusicListRes(Resource):
    def get(self):
        with codecs.open(MUSIC_PATH, 'r', 'utf-8-sig') as data_file:
            return json.load(data_file)

class VlogListRes(Resource):
    def get(self):
        with codecs.open(VLOG_PATH, 'r', 'utf-8-sig') as data_file:
            return json.load(data_file)
            
class ComedyListRes(Resource):
    def get(self):
        with codecs.open(COMEDY_PATH, 'r', 'utf-8-sig') as data_file:
            return json.load(data_file)

api.add_resource(CookListRes, "/api/cook")
api.add_resource(MusicListRes, "/api/music")
api.add_resource(VlogListRes, "/api/vlog")
api.add_resource(ComedyListRes, "/api/comedy")

if __name__ == '__main__':
    app.run()
