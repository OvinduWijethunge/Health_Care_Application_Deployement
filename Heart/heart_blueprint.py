from flask import Flask, render_template, Blueprint, request, jsonify
import pickle
import numpy as np


#home_bp = Blueprint('home_bp', __name__, template_folder='templates',static_folder='static')
heart_bp = Blueprint('heart_bp', __name__ ,template_folder='templates',static_folder='static')

classifier = pickle.load(open('Heart/random_forest_cancer.pkl', 'rb'))

@heart_bp.route('/heart')
def heart():

    
    return render_template('heart.html')
    #return 'hello'

def ValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==7):
        pred = classifier.predict(to_predict)
    return pred[0]



@heart_bp.route('/predict_heart', methods = ["POST"])
def predict_heart():
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
    #return 'wwwwwwwwwwwwwoooooooooooooo'    