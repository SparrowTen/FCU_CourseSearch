from flask import Flask

from getCourse import getCourse_blp
from getIdList import getIdList_blp
from login import login_blp

app = Flask(__name__)

app.register_blueprint(getCourse_blp, url_prefix = '/API')
app.register_blueprint(getIdList_blp, url_prefix = '/API')
app.register_blueprint(login_blp, url_prefix = '/API')

login_manager = LoginManager()
login_manager.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)