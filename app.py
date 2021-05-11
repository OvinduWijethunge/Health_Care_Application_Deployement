from flask import Flask
from Home.home_blueprint import home_bp
from Heart.heart_blueprint import heart_bp
from Diabetes.diabetes_blueprint import diabetes_bp
from Breast.breast_blueprint import breast_bp
from Liver.liver_blueprint import liver_bp

app = Flask(__name__)
app.register_blueprint(home_bp)
app.register_blueprint(heart_bp)
app.register_blueprint(diabetes_bp)
app.register_blueprint(breast_bp)
app.register_blueprint(liver_bp)



if __name__ == "__main__":
    app.run(debug=True)