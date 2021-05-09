from Health_Care_Application_Deployement import app
import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template



# Load the Random Forest CLassifier model
#filename = 'random_forest_regression_model_v2.pkl'
#classifier = pickle.load(open(filename, 'rb'))

classifier = pickle.load(open('./random_forest_cancer.pkl', 'rb'))


# Load the Random Forest CLassifier model
#filename = 'random_forest_regression_model_v2.pkl'
#classifier = pickle.load(open(filename, 'rb'))

"""def ValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==5):
        loaded_model = classifier.predict('xgboost_cancer.pkl')
        result = loaded_model.predict(to_predict)
    return result[0]
"""
@app.route('/predict_breast', methods = ["POST"])
def predict_breast():
    result=0
    if request.method == "POST":

       concave_points_mean = int(request.form['concave_points_mean'])
       area_mean = int(request.form['area_mean'])
       radius_mean = int(request.form['radius_mean'])
       perimeter_mean = int(request.form['perimeter_mean'])
       concavity_mean = int(request.form['concavity_mean'])
       
       data = np.array([[concave_points_mean,area_mean,radius_mean,perimeter_mean,concavity_mean]])
       df = pd.DataFrame(data)
       result = classifier.predict(df.values)
       
    if(int(result)==1):
        prediction = "probobly you are in a danger zone... meet a doctor immediatly"
    else:
        prediction = "Nice!! probably you are helthy!!"
    return(render_template("result.html", prediction_text=prediction))       
       
       
       
       
       #to_predict_list = request.form.to_dict()
       # to_predict_list = list(to_predict_list.values())
       # to_predict_list = list(map(float, to_predict_list))
         #cancer
        #if(len(to_predict_list)==5):
           # result = ValuePredictor(to_predict_list,5)