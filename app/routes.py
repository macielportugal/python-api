import os

from flask import Flask, jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager


app = Flask(__name__)

if 'APP_CONFIG_FILE' in os.environ:
	app.config.from_envvar('APP_CONFIG_FILE')
else:
	app.config.from_pyfile('config/production.py')

db = SQLAlchemy(app)
@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWTManager(app)

import views, models

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return models.RevokedTokenModel.is_jti_blacklisted(jti)

api = Api(app)
api.add_resource(views.ImageProcessor, '/send/image')
api.add_resource(views.UserRegistration, '/registration')
api.add_resource(views.UserLogin, '/login')
api.add_resource(views.UserLogoutAccess, '/logout/access')
api.add_resource(views.UserLogoutRefresh, '/logout/refresh')
api.add_resource(views.TokenRefresh, '/token/refresh')
api.add_resource(views.AllUsers, '/users')