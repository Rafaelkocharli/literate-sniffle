from flask import Flask, send_file

app = Flask(__name__)

@app.route('/image/<image>')
def index(image):
    return send_file(id, mimetype='image/jpg')