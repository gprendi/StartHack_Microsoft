from flask import Flask

app= Flask(__name__)

@app.route('/')
def Index():
    return 'Index'


@app.route('/output')
def Output_page():
    return 'Output'