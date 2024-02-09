import json

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/training/<prof>')
def index(prof):
    return render_template('index.html', title=prof, speciality=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
