import os
import glob
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import renamer as rename
import pdfConvert as convert
import ocr as ocr
import datetime
import sqlconnect
from dateutil import parser
import inject
import findLatestFile

###########Set folder#########################
UPLOAD_FOLDER = './uploads/'
ALLOWED_EXTENSIONS = set(['pdf'])

app = Flask(__name__, static_url_path = "/images", static_folder = "images")
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

################################################################
@app.route('/upload')
def uploaded_file():
    #Rename pdf to datetime
    rename.rename_pdf()
    #rename image
    ocr.ocr(rename.rename_png())
    latest_file = findLatestFile.latestImg()
    latest_txt = findLatestFile.latestTxt()
    inject.inject_sql(latest_txt)

    return render_template('upload.html', latest_file=latest_file)
#################################################################

@app.route('/help', methods=['GET', 'POST'])
def help_page():
        return render_template('help.html')

###############################################################

@app.route('/reports')
def reports():
    return render_template('reports.html')#, files=files)

#######################################################################
@app.route('/reports1', methods = ['POST','GET'])
def date_range():
    if request.method == 'POST':
        dateDict = request.form.to_dict()
        startD = dateDict.get('sday')
        startDT = parser.parse(startD)
        endD = dateDict.get('eday')
        endDT = parser.parse(endD)
        todayDT = parser.parse(datetime.datetime.today().strftime('%Y-%m-%d'))

        if startDT <= endDT and endDT <= todayDT:
            sql_query = "Select * from Report_T \
            WHERE ReportDate BETWEEN \"{}\" AND \"{}\"".format(startD, endD)
            sqlDict = sqlconnect.runQuery(sql_query)
            return render_template('reports1.html', sqlDict=sqlDict)
        else:
            wrongDate = True
            return render_template('reports1.html', wrongDate=wrongDate)
###############################################################

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    app.run(debug=False)
    app.secret_key = "87098jlakjhf8slkjH&"
