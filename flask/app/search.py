from flask import Blueprint, request, render_template, url_for, redirect
import json
import requests

search_blp = Blueprint('search_blp', __name__, template_folder= 'templates')

@search_blp.route('/submit', methods=['GET', 'POST'])
def submit():
    print('test')
    if request.method == 'POST':
        Class_id = request.form['Classid']
        return redirect(url_for('search_blp.result', Classid = Class_id))
    else:
        return render_template('index.html')

@search_blp.route('/result/<Classid>')
def result(Classid):
    r = requests.get(f"http://localhost:5000/API/getCourse?year=111&sms=1&cls_id={Classid}")
    r = json.loads(r.text)
    print(r)
    return render_template('result.html',data = r)