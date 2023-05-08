from flask import Flask

from getCourse import getCourse_blp
from Id import id_blp
from Course import course_blp
from login import login_blp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(getCourse_blp, url_prefix = '/API')
app.register_blueprint(id_blp, url_prefix = '/API/Id')
app.register_blueprint(login_blp, url_prefix = '/API/Login')
app.register_blueprint(course_blp, url_prefix = '/API/Course')

if __name__ == '__main__':
    app.run(debug=True,host="127.0.0.1")