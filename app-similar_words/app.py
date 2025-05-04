from flask import Flask, jsonify, request, make_response

import requests

similars_app = Flask(__name__)

def get_model(model_name):
    match model_name:
        case "custom":
            return "glove-twitter-50"
        case _:
            return "glove-twitter-25"


@similars_app.route('/similar', methods=['GET'])
def get_similars():
    # Now 'word' is directly passed from the URL
    _model = request.args.get('model', default="custom")
    _word = request.args.get('word')
    _topn = request.args.get('topn', type=int, default=10)

    print(f"word:{_word} ; _topn:{_topn}")

    match _model:
        case "custom":
            extract = requests.get(f'http://127.0.0.1:5000/model?word={_word}&topn={_topn}')
            if extract.status_code == 200:
                response = make_response(jsonify(extract.json()), 200)
                response.headers['Access-Control-Allow-Origin'] = '*'
                return response
            else:
                response = make_response("Error fetching data from model1", 500)
                response.headers['Access-Control-Allow-Origin'] = '*'
                return response
        case _:
            extract = requests.get(f'http://127.0.0.1:5001/model?word={_word}&topn={_topn}')
            if extract.status_code == 200:
                response = make_response(jsonify(extract.json()), 200)
                response.headers['Access-Control-Allow-Origin'] = '*'
                return response
            else:
                response = make_response("Error fetching data from model1", 500)
                response.headers['Access-Control-Allow-Origin'] = '*'
                return response
    
if __name__ == "__main__":
    similars_app.run(debug=True)
