from flask import Flask
from flask_login import LoginManager

from getCourse import getCourse_blp
from getIdList import getIdList_blp
from getAccount import getAccount_blp

app = Flask(__name__)

app.register_blueprint(getCourse_blp, url_prefix = '/API')
app.register_blueprint(getIdList_blp, url_prefix = '/API')
app.register_blueprint(getAccount_blp, url_prefix = '/API')

login_manager = LoginManager()
login_manager.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
    login_manager = LoginManager(app)