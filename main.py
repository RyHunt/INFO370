import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug import secure_filename

UPLOAD_FOLDER = '/home/ryanmhunt/INFO370/uploads/'
ALLOWED_EXTENSIONS = set(['pdf'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect('/uploads')
    return render_template('index.html')

@app.route('/uploads', methods=['GET', 'POST'])
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

'''from flask import send_from_directory

@app.route('/upload', methods=['GET', 'POST'])
def uploaded_file():
    return render_template('upload.html')

#@app.route('/upload', methods=['GET', 'POST'])
#def uploaded():
#        return render_template('upload.html')

@app.route('/reports', methods=['GET', 'POST'])
def reports():
        return render_template('reports.html')

@app.route('/help', methods=['GET', 'POST'])
def help_page():
        return render_template('help.html')
'''
if __name__ == '__main__':
    app.run(host='0.0.0.0')
    app.run(debug=False)
    app.secret_key = "87098jlakjhf8slkjH&"
