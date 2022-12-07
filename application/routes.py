import random
from application import app
from flask import render_template, request, json, jsonify
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
import requests
import numpy
import pandas as pd
import json

#decorator to access the app
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

#decorator to access the service
@app.route("/strokedetect", methods=['GET', 'POST'])
def strokedetect():

    #extract form inputs
    age = request.form.get("age") 
    heart_disease = request.form.get("heart_disease") 
    average_glucose_level = request.form.get("average_glucose_level")
    # persons = request.form.get("persons")
    # lug_boot = request.form.get("lug_boot")
    # safety = request.form.get("safety")

    #extract data from json
    input_data = json.dumps({"buying": age, "heart_disease": heart_disease, "average_glucose_level": average_glucose_level})

    #url for stroke classification api
    url = "http://127.0.0.1:8000/api"

 
    #post data to url
    results =  requests.post(url, input_data)
    content =results.content.decode('UTF-8')
    content=json.loads(content)
    #send input values and prediction result to index.html for display
    return render_template("index.html", age = age, heart_disease = heart_disease, average_glucose_level = average_glucose_level, results=2, accuracy=accuracy, pred=pred)
  
