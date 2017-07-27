from flask import Flask
from flask_restful import Resource, Api, reqparse
import json
import codecs
import os


APP_ROOT = os.path.dirname(os.path.abspath(__file__))
VIDEO_PATH = os.path.join(APP_ROOT, "video.json")

app = Flask(__name__)
api = Api(app)

class VideoListRes(Resource):
    def get(self):
        with codecs.open(VIDEO_PATH, 'r', 'utf-8-sig') as data_file:
            return json.load(data_file)

api.add_resource(VideoListRes, "/api/video")

if __name__ == '__main__':
    app.run()
