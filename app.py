from flask import Flask #importing the constructor

app = Flask(__name__) #app generated

from controllers import controller #controller imports app 

if __name__ == "__main__":
    app.run(debug=True)