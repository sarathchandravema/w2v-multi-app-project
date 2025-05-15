import streamlit as st
import pandas as pd
import common_functions as cf

st.title("Similarity Search")
st.write("This is a simple app to fetch similar using pre-trained word2Vec models.")


if "page" not in st.session_state:
    st.session_state.page = "home"

# if "content" not in st.session_state:
#     st.session_state.content = {}

if "disabled" not in st.session_state:
    st.session_state.disabled = False

def disable():
    st.session_state.disabled = True

# def fetch_similar_words():
#     word = st.session_state.content["word"]
#     topn = st.session_state.content["topn"]
#     model = st.session_state.content["model"]

#     if word and topn:
#         st.write(f"Fetching similar words for '{word}' using the '{model}' model with top {topn} results.")
#         # Call the function from common_functions.py
#         st.write(cf.sample_function(word))
        
#         st.session_state.page = "results"
#     # else:
    #     st.write("testing")
    #     st.write("Please enter a word and select the number of similar words.")

def back_to_home():
    st.session_state.page = "home"
    st.session_state.disabled = False
    st.session_state.word = ""
    # st.session_state.topn = 
    st.session_state.model = "small"
    # st.session_state.content = {}

# def go_to_results(data):
def go_to_results():
    st.session_state.page = "results"
    # st.write(f"Word: {data['word']}")
    # st.write(f"Top N: {data['topn']}")
    # st.write(f"Model: {data['model']}")
    # st.session_state.disabled = True

print(f"1: {st.session_state.page}")
if st.session_state.page == "home":
    # st.text_input("Enter a word for similarity search", key="word", disabled=st.session_state.disabled, on_change=disable)
    # st.number_input("Number of similar words", min_value=1, max_value=300, value=10, step=1, key="topn", disabled=st.session_state.disabled, on_change=disable)
    # st.radio("Select a model", ("small", "medium"), key="model", disabled=st.session_state.disabled, on_change=disable)

    st.text_input("Enter a word for similarity search", key="word")#, value=st.session_state.content.get("word", ""))
    st.number_input("Number of similar words", min_value=1, max_value=300, value=10, step=1, key="topn")
    st.radio("Select a model", ("small", "medium"), key="model")

    # word_ = st.text_input("Enter a word for similarity search", key="word", disabled=st.session_state.disabled, on_change=disable)
    # topn_ = st.number_input("Number of similar words", min_value=1, max_value=300, value=10, step=1, key="topn", disabled=st.session_state.disabled, on_change=disable)
    # model_ = st.radio("Select a model", ("small", "medium"), key="model", disabled=st.session_state.disabled, on_change=disable)
    
    # st.session_state.content["word"] = word_
    # st.session_state.content["topn"] = topn_
    # st.session_state.content["model"] = model_
    
    # st.button("Get Similar Words", on_click=go_to_results,args=(st.session_state.content,), key="submit_button")#:
    st.button("Get Similar Words", on_click=go_to_results, key="submit_button")
        # st.session_state.page = "results"




if st.session_state.page == "results":
    st.write("Similar words fetched successfully!")
    # st.write(st.session_state.content)

    # st.write(f"Word: {st.session_state.word}")
    # st.write(f"Top N: {st.session_state.topn}")
    # st.write(f"Model: {st.session_state.model}")

    st.text_input("Enter a word for similarity search", key="word")#, value=st.session_state.content.get("word", ""), disabled=True)
    st.number_input("Number of similar words", min_value=1, max_value=300, value=10, step=1, key="topn", disabled=True)
    st.radio("Select a model", ("small", "medium"), key="model", disabled=True)

    fetched_words = cf.get_similar_words(st.session_state.word, st.session_state.topn, st.session_state.model)

    # st.write(cf.sample_function(st.session_state.word))
    st.write(pd.DataFrame(fetched_words, columns=["Word", "Similarity"]))
    st.button("Back to Home", on_click=back_to_home, key="back_button")

# else:
#     st.write("Fetching similar words...")
#     st.button("Back to Home", on_click=lambda: st.session_state.update(home_page=True, word="", topn=10, model="small"))

print(f"2: {st.session_state.page}")