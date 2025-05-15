from flask import Flask, request, make_response
from gensim import downloader as gensim_loader

model2_app = Flask(__name__)

@model2_app.route('/model', methods=['GET'])
def get_similars():
    
    _model = gensim_loader.load("glove-twitter-50")
    _word = request.args.get('word')
    _topn = request.args.get('topn', type=int, default=10)
    
    print(f"Using glove-twitter-50 => word:{_word} ; _topn:{_topn}")
    
    if _word:
        # Process the word (e.g., find similar words)
        similars = _model.most_similar(_word, topn=_topn)
        response = make_response(dict(similars), 200)
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
    return "No word provided", 400
        
if __name__ == "__main__":
    model2_app.run(debug=True)