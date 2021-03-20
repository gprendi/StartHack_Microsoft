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
#Redirect to index
@app.route('/')
def home():
    return redirect(url_for('index'))
#index
@app.route('/index', methods=['GET','POST'])
def index():
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
            return redirect(url_for('output_page', filename= filename))
    return render_template('index.html')

@app.route('/output/<filename>')
def output_page(filename):
    return 'Output of %s'%(filename)


