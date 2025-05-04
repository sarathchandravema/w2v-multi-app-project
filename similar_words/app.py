from flask import Flask, render_template, request, make_response
from gensim import downloader as gensim_loader


similar_words_app = Flask(__name__)

model = gensim_loader.load('glove-twitter-25')

@similar_words_app.route('/similar', methods=['GET'])
def get_similars():
    # Now 'word' is directly passed from the URL
    word = request.args.get('word')
    _topn = request.args.get('topn', type=int, default=10)
    print(f"word:{word} ; _topn:{_topn}")
    if word:
        # Process the word (e.g., find similar words)
        similars = model.most_similar(word, topn=_topn)
        response = make_response(dict(similars), 200)
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
    return "No word provided", 400
    
    
if __name__ == "__main__":
    similar_words_app.run(debug=True)
