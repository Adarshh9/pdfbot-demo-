from flask import Flask , request , jsonify
from pdfchatbot import pdfqna , PALM_API_KEY

app = Flask(__name__)


@app.route("/home", methods=['GET'])
def home():
    return "HOME PAGE"


@app.route("/get_response", methods=['POST'])
def get_response():
    query = request.form['query']
    
    response = pdfqna(query)
    
    response = jsonify({
        'response': response
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == '__main__':
    app.run(port=5001)