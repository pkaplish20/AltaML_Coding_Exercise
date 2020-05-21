import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from coding_exercise import get_coordinates

app = Flask(__name__)


# render index.html from temlates folder
@app.route('/')
def home():
    return render_template('index.html')


# post the text file to api and get the coordinates of path traveled and orientation
@app.route('/uploadFile', methods=['POST'])
def extractInfo():
    files = request.files.getlist('file')  # get the file from frontend
    files[0].seek(0)
    data = files[0].read().decode('UTF-8')  # read the file
    coord, orientation = get_coordinates(data)
    return jsonify({'coordinates_list': coord, 'last_orientation': orientation})

if __name__ == '__main__':
    app.run(debug=True, port=5000) 
