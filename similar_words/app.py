from flask import Flask, render_template, request
from gensim import downloader as gensim_loader


similar_words_app = Flask(__name__)

model = gensim_loader.load('glove-twitter-25')

@similar_words_app.route('/similar', methods=['GET'])
def get_similars():
    # Now 'word' is directly passed from the URL
    word = request.args.get('word')
    if word:
        # Process the word (e.g., find similar words)
        similars = model.most_similar(word, topn=10)
        return {"message":f"Similar words for: {word} are {[i[0] for i in similars]}"}, 200
    return "No word provided", 400
    
    
if __name__ == "__main__":
    similar_words_app.run(debug=True)
