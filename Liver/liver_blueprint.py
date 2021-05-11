from flask import Flask, render_template, Blueprint, request, jsonify
import pickle
import numpy as np

#home_bp = Blueprint('home_bp', __name__, template_folder='templates',static_folder='static')
liver_bp = Blueprint('liver_bp', __name__ ,template_folder='templates',static_folder='static')

classifier = pickle.load(open('Liver/random_forest_liver.pkl', 'rb'))

@liver_bp.route('/liver')
def liver():

    
    return render_template('liver.html')
    #return 'hello'

def ValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==7):
        pred = classifier.predict(to_predict)
    return pred[0]



@liver_bp.route('/predict_liver', methods = ["POST"])
def predict_liver():
    result = 0
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
         #diabetes
        if(len(to_predict_list)==7):
            result = ValuePredictor(to_predict_list,7)
    
    
    return(render_template("result.html", prediction_text=result))
    #return 'wwwwwwwwwwwwwoooooooooooooo'    