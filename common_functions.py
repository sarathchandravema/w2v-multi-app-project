from gensim import downloader as gensim_loader
import pandas as pd

def create_df(data):
    """
    Create a DataFrame from the given data.
    
    Args:
        data (list): A list of tuples containing word and its vector.
        
    Returns:
        pd.DataFrame: A DataFrame containing words and their vectors.
    """
    # create index for the DataFrame
    index = range(1, len(data)+1)
    
    # create a DataFrame from the data
    df = pd.DataFrame(data, columns=["Word", "Similarity Score"], index=index)
        
    return df


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
    similar_words = model.most_similar(word.lower(), topn=topn)

    return create_df(similar_words)


def get_analogy_words(word1, word2, word3, topn, model_name):
    """
    Fetch analogy words from the specified model.
    
    Args:
        word1 (str): The first word in the analogy.
        word2 (str): The second word in the analogy.
        word3 (str): The third word in the analogy.
        model_name (str): The model to use for fetching analogy words.
        
    Returns:
        list: A list of tuples containing analogy words and their similarity scores.
    """
    print(f"Fetching analogy words for '{word1}', '{word2}', and '{word3}' using the '{model_name}' model.")
    
    # fetch the model by name
    if model_name == "small":
        model = gensim_loader.load("glove-twitter-25")
    elif model_name == "medium":
        model = gensim_loader.load("glove-twitter-50")
    else:
        model = gensim_loader.load("glove-twitter-25")
        
    # fetch analogy words
    analogy_words = model.most_similar(positive=[word1.lower(), word3.lower()], negative=[word2.lower()], topn=topn)

    return create_df(analogy_words)