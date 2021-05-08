from Health-Care-Application-Deployement import app
import pickle
import numpy as np
from flask import Flask, request, jsonify, render_template
#@app.route('/hello')
#def hello():
 #   return 'Hello World!'
classifier = pickle.load(open('xgboost_cancer.pkl', 'rb'))


# Load the Random Forest CLassifier model
#filename = 'random_forest_regression_model_v2.pkl'
#classifier = pickle.load(open(filename, 'rb'))

def ValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==5):
        loaded_model = classifier.predict('xgboost_cancer.pkl')
        result = loaded_model.predict(to_predict)
    return result[0]

@app.route('/predict_breast', methods = ["POST"])
def predict_breast():
    result=0
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
         #cancer
        if(len(to_predict_list)==5):
            result = ValuePredictor(to_predict_list,5)
    
    if(int(result)==1):
        prediction = "situation is not goood "
    else:
        prediction = "No cancer"
    return(render_template("result.html", prediction_text=prediction))      