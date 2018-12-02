import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import renamer as rename
import pdfConvert as convert
import ocr as ocr

UPLOAD_FOLDER = './uploads/'
ALLOWED_EXTENSIONS = set(['pdf'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

###############set Home--
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'sales.pdf'))
            #convert PDF
            convert.pdfConvert()
            return redirect(url_for('uploaded_file'))
    return render_template('index.html')


@app.route('/upload')
def uploaded_file():
    #Rename pdf to datetime
    rename.rename_pdf()
    #rename image
    ocr.ocr(rename.rename_png())
    return render_template('upload.html')

'''
from flask import send_from_directory

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)'''

@app.route('/help', methods=['GET', 'POST'])
def help_page():
        return render_template('help.html')

@app.route('/reports', methods=['GET', 'POST'])
def reports():
        return render_template('reports.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    app.run(debug=False)
    app.secret_key = "87098jlakjhf8slkjH&"
