from flask import Flask
from api.database import db
from .views.item import item
# import api.config as config

# def create_app():

app = Flask(__name__)

# DB設定を読み込む
app.config.from_object('api.config.DevelopmentConfig')
db.init_app(app)

app.register_blueprint(item, url_prefix='/item')

#     return app

# app = create_app()