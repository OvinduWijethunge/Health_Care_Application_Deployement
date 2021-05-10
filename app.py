from flask import Flask
from Home.home_blueprint import home_bp
from Heart.heart_blueprint import heart_bp

app = Flask(__name__)
app.register_blueprint(home_bp)
app.register_blueprint(heart_bp)



if __name__ == "__main__":
    app.run(debug=True)