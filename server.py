from flask import Flask, jsonify
from flask import *

app = Flask(__name__)


@app.route('/get', methods=['GET'])
def get():
    with open("file.json", "r") as f:
        return f.read()

@app.route('/post', methods=['POST'])
def create_task():
    if not request.json:
        abort(400)
    with open("file.json", "w") as f:
        f.write(json.dumps(request.json))
    return json.dumps(request.json), 201

@app.route('/')
def show():
    return render_template('wiki.html')

if __name__ == '__main__':
    app.run()