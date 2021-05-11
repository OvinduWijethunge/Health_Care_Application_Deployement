from flask import Flask, render_template, Blueprint, request, jsonify
import pickle
import numpy as np
import pandas as pd

#home_bp = Blueprint('home_bp', __name__, template_folder='templates',static_folder='static')
breast_bp = Blueprint('breast_bp', __name__ ,template_folder='templates',static_folder='static')

classifier = pickle.load(open('Breast/random_forest_cancer.pkl', 'rb'))

@breast_bp.route('/breast')
def breast():

    
    return render_template('breast.html')
    #return 'hello'

def ValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==5):
        pred = classifier.predict(to_predict)
    return pred[0]



@breast_bp.route('/predict_breast', methods = ["POST"])
def predict_breast():
    result = 0
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
         #diabetes
        if(len(to_predict_list)==5):
            result = ValuePredictor(to_predict_list,5)
    
    if(int(result)==1):
        prediction = "probobly you are in a danger zone... meet a doctor immediatly"
    else:
        prediction = "Nice!! probably you are helthy!!"
    return(render_template("result.html", prediction_text=prediction))
    #return 'wwwwwwwwwwwwwoooooooooooooo'    