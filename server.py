from flask import Flask, jsonify
from flask import render_template, url_for

app = Flask(__name__)
if __name__ == '__main__':
    app.run()


@app.route('/get', methods=['GET'])
def get():
    with open("file.json", r) as f:
        return jsonify(f.read())

@app.route('/post', methods=['POST'])
def create_task():
    if not request.json:
        abort(400)
    with open("file.json", r) as f:
        f.write(str(request.json))
    return str(request.json), 201

url_for('static', filename='jquery-3.1.1.js')
url_for('static', filename='wiki.html')
