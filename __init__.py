import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from coding_exercise import get_coordinates

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/uploadFile', methods=['POST'])
def extractInfo():
    files = request.files.getlist('file')
    files[0].seek(0)
    data = files[0].read().decode('UTF-8')
    coord, orientation = get_coordinates(data)
    for f in files:
        file_location = os.path.join(os.getcwd()+'/Uploads', secure_filename(f.filename))
        f.save(file_location)
    return jsonify({'coordinates_list': coord, 'last_orientation': orientation})

if __name__ == '__main__':
    app.run(debug=True, port=5000) 