# Health Care App - Deployment
<p align=left>
<img src="https://img.shields.io/badge/Type-Classification-blue"/> 
<img src="https://img.shields.io/badge/Python-3.9-brightgreen"/>
<img src="https://img.shields.io/badge/DataSet-Kaggle-brightgreen"/> 
<p/>
<br>
<p align=center>
<img src="https://media.giphy.com/media/1PC0bKpeSM8WxKRfjH/giphy.gif" width="500px" height="300px"> 
</p>
<br>
<br>
• This project predicts whether a person has a below diseases or not and it is need to know particular disease features for do the prediction.
      
      1. Heart Disease
      2. Diabetes
      3. Liver Disease
      4. Kidney Disease
    
 
• This repository consists of files required to deploy a ___WEB APPLICATION___ created with ___Flask___ on ___Heroku___ platform.

• Data set got from kaggle, if you want to inspect it just click below links for each diseases. 

  Link for Heart Disease Dataset  = _https://www.kaggle.com/johnsmith88/heart-disease-dataset_ <br>
  Link for Diabetes Disease Dataset = _https://www.kaggle.com/uciml/pima-indians-diabetes-database_ <br>
  Link for Liver Disease Dataset = _https://www.kaggle.com/uciml/indian-liver-patient-records_ <br>
  Link for Kidney Disease Dataset = _https://www.kaggle.com/mansoordaku/ckdisease_ <br>
    

• You can see deployed model in heroku , use below link for reach to deployed model:<br />
  Heroku: _https://health-care-app-v1.herokuapp.com/_

• If you want to check the algorithems, EDA phases, feature engineering phases ,models which used for implemented the model and see the accuracy matrix just Click the link mentioned below:<br />
Link: _https://github.com/OvinduWijethunge/Machine_Learning_Projects_

<hr>


### If you are willing to check project in flask API


### Prerequisites
You must have Scikit Learn, Pandas (for Machine Leraning Model) and Flask (for API) installed.

### Project Structure
This project has four major parts :
1. blueprints - These folders containing relevent prediction algorithm files, models pkl files for each diseasess.
2. app.py - Entry point, This contains Flask APIs that receives diseasess details through GUI.
3. static - This uses for store css files, images and some gifs for while presenting.
4. templates - This folder contains the HTML template to allow user to enter required detail and displays the predicted diseasess.


### Running the project in FLASK
type flask run for start your server. (if you want to enable debugger mode just type set FLASK_ENV=development as the first CLI command) <br>
then copy the given url and paste it in your browser. <br>
then input valid inputs do predictions. <br>
