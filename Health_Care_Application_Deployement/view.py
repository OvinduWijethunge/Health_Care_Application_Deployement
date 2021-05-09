from Health_Care_Application_Deployement import app
import pickle
import numpy as np
from flask import Flask, request, jsonify, render_template
#@app.route('/hello')
#def hello():
 #   return 'Hello World!'
classifier = pickle.load(open('xgboost_heart_disease.pkl', 'rb'))


# Load the Random Forest CLassifier model
#filename = 'random_forest_regression_model_v2.pkl'
#classifier = pickle.load(open(filename, 'rb'))

def ValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==7):
        pred = classifier.predict(to_predict)
    return pred[0]

@app.route('/predict', methods = ["POST"])
def predict():
    result = 0
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
         #diabetes
        if(len(to_predict_list)==7):
            result = ValuePredictor(to_predict_list,7)
    
    if(int(result)==1):
        prediction = "probobly you are in a danger zone... meet a doctor immediatly"
    else:
        prediction = "Nice!! probably you are helthy!!"
    return(render_template("result.html", prediction_text=prediction))  