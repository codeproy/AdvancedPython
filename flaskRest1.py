from flask import Flask,abort,jsonify, request

app = Flask(__name__)

@app.route('/api')

def make_predict():
    return (jsonify({"name" : "Hello World"}))

if __name__ == '__main__':
    app.run( debug=True)
