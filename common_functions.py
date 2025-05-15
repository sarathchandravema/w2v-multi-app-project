from gensim import downloader as gensim_loader

def get_similar_words(word, topn, model_name):
    """
    Fetch similar words from the specified model.
    
    Args:
        word (str): The word to find similar words for.
        topn (int): The number of similar words to fetch.
        model_name (str): The model to use for fetching similar words.
        
    Returns:
        list: A list of tuples containing similar words and their similarity scores.
    """
    print(f"Fetching similar words for '{word}' using the '{model_name}' model with top {topn} results.")
    
    # fetch the model by name
    if model_name == "small":
        model = gensim_loader.load("glove-twitter-25")
    elif model_name == "medium":
        model = gensim_loader.load("glove-twitter-50")
    else:
        model = gensim_loader.load("glove-twitter-25")
        
    # fetch similar words
    similar_words = model.most_similar(word, topn=topn)

    return similar_words