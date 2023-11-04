from flask import Flask, request, jsonify
from pdfchatbot import pdfqna, PALM_API_KEY

app = Flask(__name__)

@app.route("/home", methods=['GET'])
def home():
    return "HOME PAGE"

@app.route("/get_response", methods=['GET','POST'])
def get_response():
    data = request.get_json()  
    query = data.get('query')

    if query is not None:
        response = pdfqna(query)
        response = jsonify({
            'response': response
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    else:
        return jsonify({
            'error': 'Invalid request, query missing'
        }), 400  

if __name__ == '__main__':
    app.run(port=5001)
