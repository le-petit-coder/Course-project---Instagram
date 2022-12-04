import os

from flask import Flask
from main.views import main_blueprint
# from db import db

app = Flask(__name__)
# db.init_db(app)
app.register_blueprint(main_blueprint)
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
DB_HOST = 'db'
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_NAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.errorhandler(404)
def page_error_404(error):
    return f"Такой страницы нет {error}", 404


@app.errorhandler(500)
def page_error_500(error):
    return f"На сервере ошибка - {error}", 500


if __name__ == "__main__":
    app.run(port=25000)