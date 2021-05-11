from flask import Flask, render_template, Blueprint, request, jsonify
import pickle


#home_bp = Blueprint('home_bp', __name__, template_folder='templates',static_folder='static')
diabetes_bp = Blueprint('diabetes_bp', __name__ ,template_folder='templates',static_folder='static')

classifier = pickle.load(open('Diabetes/random_forest_diabetes.pkl', 'rb'))

@diabetes_bp.route('/diabetes')
def diabetes():

    
    return render_template('diabetes.html')
    #return 'hello'

def ValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==6):
        pred = classifier.predict(to_predict)
    return pred[0]



@diabetes_bp.route('/predict_diabetes', methods = ["POST"])
def predict_diabetes():
    result = 0
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
         #diabetes
        if(len(to_predict_list)==6):
            result = ValuePredictor(to_predict_list,6)
    
    if(int(result)==1):
        prediction = "probobly you are in a danger zone... meet a doctor immediatly"
    else:
        prediction = "Nice!! probably you are helthy!!"
    return(render_template("result.html", prediction_text=prediction))
    #return 'wwwwwwwwwwwwwoooooooooooooo'    