from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
import os
from OCR import OCR_PDF
from TTS import tts


##CONSTANTS DECLARATION FOR UPLOADING FILES

UPLOAD_FOLDER = './uploads/'
ALLOWED_EXTENSIONS = {'txt','pdf','png','jpeg'}

##APP STARTUP 
app= Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key='blabla'


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS
    
#Redirect to index
@app.route('/')
def home():
    return redirect(url_for('index'))
    
#index
@app.route('/index', methods=['GET','POST'])
def index():
    error = None
    if request.method == 'POST':
        ##CHECK IF THE POST REQUEST HAS A FILE WITHIN IT
        if 'file' not in request.files:
            error ='No file was given please input a valid file'
            
        file = request.files['file']
        
        #If user does not select file, browser also
        #submit an empty part without filename
        if file.filename == '':
            error ='No Selected file. Please insert your file.'
           
        if not allowed_file(file.filename):
            error ='Wrong file Format. Please try again with either of these: .pdf .png .jpeg .txt'
            
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('output_page', filename= filename))
    return render_template('index.html', error=error)

@app.route('/output/<filename>')
def output_page(filename):
    return 'Output of %s'%(filename)


if __name__ == "__main__":
    app.run()