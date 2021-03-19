from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
import os

##CONSTANTS DECLARATION FOR UPLOADING FILES

UPLOAD_FOLDER = './uploads/'
ALLOWED_EXTENSIONS = {'txt','pdf','png','jpeg'}

##APP STARTUP 
app= Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        ##CHECK IF THE POST REQUEST HAS A FILE WITHIN IT
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        #If user does not select file, browser also
        #submit an empty part without filename
        if file.filename == '':
            flash('No Selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename= filename))
    return render_template('index.html')

@app.route('/output')
def Output_page():
    return 'Output'


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)