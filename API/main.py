from flask import Flask

from getCourse import getCourse_blp
from getIdList import getIdList_blp
from Course import Course_blp
from Login import login_blp

app = Flask(__name__)

app.register_blueprint(getCourse_blp, url_prefix = '/API')
app.register_blueprint(getIdList_blp, url_prefix = '/API')
app.register_blueprint(login_blp, url_prefix = '/API/Login')
app.register_blueprint(Course_blp, url_prefix = '/API/Course')

if __name__ == '__main__':
    app.run(debug=True)