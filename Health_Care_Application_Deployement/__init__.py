import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
#model = pickle.load(open('model.pkl', 'rb'))

import Health_Care_Application_Deployement.view as hrt
import Health_Care_Application_Deployement.breast as bre

@app.route('/')
def home():

    
    return render_template('index.html')


@app.route("/heart", methods=['POST', 'GET'])
def heart():
    return render_template("heart.html")
    
@app.route("/breast", methods=['POST', 'GET'])
def breast():
    return render_template("breast.html")    


if __name__ == "__main__":
    app.run(debug=True)