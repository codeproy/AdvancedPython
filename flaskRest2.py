from flask import Flask,abort,jsonify, request
import requests

#url = "http://localhost:5000/api"

app = Flask(__name__)

@app.route('/api',methods=['POST','GET'])

def index():
    if (request.method == 'POST'):
        some_json = request.get_json(force=True)
#        some_json = requests.get(url).json()
#        return(requests.get(url).json())
        return (jsonify({'sent' :some_json}),201)
    else:
        return (jsonify({"namez" : "Hello Worlx"}))


@app.route('/multi/<int:num>',methods=['GET'])
            
def get_mul10(num):
    return(jsonify({'mult 10' : num * 10}))

if __name__ == '__main__':
    app.run(debug=True)
