import datetime 
import json

import requests
from flask import render_template, redirect, request

from app import app

@app.route('/')
def index():
    return render_template('index.html',
                            )