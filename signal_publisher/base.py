from flask import Flask, request
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
from redis import Redis


app = Flask(__name__)
ma = Marshmallow(app)
api = Api(app)

r = redis.Redis(host='redis', port=6379, db=0)
