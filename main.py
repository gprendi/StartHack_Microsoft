from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
import os
from OCR import OCR_PDF, OCR_image
from backend import Ds
from backend import process_text
from backend import predict
from DICTIONARYAPI import request_definition
import requests


##CONSTANTS DECLARATION FOR UPLOADING FILES

UPLOAD_FOLDER = './uploads/'
ALLOWED_EXTENSIONS = {'txt','pdf','png','jpeg'}

##APP STARTUP 
app= Flask(__name__)
app._static_folder='static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key='blabla'


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

def data_Processer(filename):
    sb = Ds()
    text =''
    if filename.rsplit('.',1)[1].lower() not in ['txt','png','jpeg']:
        text = OCR_PDF(filename)
    elif filename.rsplit('.',1)[1].lower() != 'txt':
        text = OCR_image(filename)
    else:
        with open(filename, 'r') as f:
            text = f.read()
    definitions =[]
    precautions = []
    summary = process_text(text)
    illness = predict(summary)
    print(illness)
    if illness in sb.symptom_precautions:
        for k in sb.symptom_precautions[illness]:
            precautions.append(k)

    for i in summary:
        definitions.append(request_definition(i))
    print('%s ??? %s ??? %s' % (summary,definitions,precautions))
    return ' '.join(summary), definitions, precautions
    
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
    filename = "uploads/"+filename
    summary,definitions,precautions = data_Processer(filename)
    return render_template('output.html', summary= summary, definitions=definitions, precautions=precautions)





if __name__ == "__main__":
    app.run()



    



