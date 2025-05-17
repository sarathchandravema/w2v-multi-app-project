import streamlit as st
import pandas as pd
import common_functions as cf

st.set_page_config(page_title="Similarity Search", page_icon=":mag:")
st.title("Similarity Search")


if "page" not in st.session_state:
    st.session_state.page = "home"

if "disabled" not in st.session_state:
    st.session_state.disabled = False

def disable():
    st.session_state.disabled = True


def back_to_home():
    st.session_state.page = "home"
    st.session_state.disabled = False
    st.session_state.word = ""
    st.session_state.model = "small"

def go_to_results(page):
    if page == "similar":
        st.session_state.page = "similar_results"
    elif page == "analogy":
        st.session_state.page = "analogy_results"
    else:
        st.session_state.page = "home"

def go_to_page(page):
    if page == "similar":
        st.session_state.page = "similar"
    elif page == "analogy":
        st.session_state.page = "analogy"
    else:
        st.session_state.page = "home"


print(f"1: {st.session_state.page}")
## home page
if st.session_state.page == "home":
    st.write("Welcome to the home page!")
    st.write("")
    st.write("This is an app to demonstrate the capability of simple pre-trained Word2Vector models.")
    st.write("You can search for similar words or find analogy words.")
    st.write("")
    st.button("Get Similar Words", on_click=go_to_page, args=("similar",), key="similars_button")
    st.button("Get Analogy Words", on_click=go_to_page, args=("analogy",), key="analogies_button")


## Similarity Search page
if st.session_state.page == "similar":
    st.write("Welcome to the Similarity Search page!")
    st.write("Used to find words that are similar to a given word.")
    st.write("")

    st.text_input("Enter a word for similarity search", key="word")
    st.number_input("Number of similar words", min_value=1, max_value=300, value=10, step=1, key="topn")
    st.radio("Select a model", ("small(glove-twitter-25)", "medium(glove-twitter-50)"), key="model")

    st.button("Fetch", on_click=go_to_results, args=(st.session_state.page, ), key="similar_submit")



## similarity search results page
if st.session_state.page == "similar_results":
    st.write("Similar words fetched successfully!")

    st.text_input("Enter a word for similarity search", key="word")
    st.number_input("Number of similar words", min_value=1, max_value=30, value=10, step=1, key="topn", disabled=True)
    st.radio("Select a model", ("small", "medium"), key="model", disabled=True)
    
    fetched_words = cf.get_similar_words(st.session_state.word, st.session_state.topn, st.session_state.model)
    st.write(fetched_words)
    st.button("Back to Home", on_click=back_to_home, key="back_button")
    st.button("Get Analogy Words", on_click=go_to_page, args=("analogy",), key="analogies_button") ##check if it works



## Analogy Search page
if st.session_state.page == "analogy":
    st.write("Welcome to the Analogy Search page!")
    st.write("Used to find words that are related to a given word in a specific way.")
    st.write("")

    col1, int1, col2, int2, col3, int3, col4 = st.columns(7)
    col1.text_input("Word 1", key="word1", value="king", disabled=True)
    int1.write(":")
    col2.text_input("Word 2", key="word2", value="queen", disabled=True)
    int2.write(":::")
    col3.text_input("Word 3", key="word3", value="man", disabled=True)
    int3.write(":")
    col4.text_input("Result", key="result_word", value="woman", disabled=True)

    st.text_input("Enter a word for analogy search", key="analogy_word1")
    st.text_input("Enter a second word for analogy search", key="analogy_word2")
    st.text_input("Enter a third word for analogy search", key="analogy_word3")
    
    st.number_input("Number of nearest words", min_value=1, max_value=30, value=10, step=1, key="analogy_topn")
    
    st.radio("Select a model", ("small(glove-twitter-25)", "medium(glove-twitter-50)"), key="analogy_model")

    st.button("Fetch", on_click=go_to_results, args=(st.session_state.page, ), key="analogy_submit")


## Analogy Search results page
if st.session_state.page == "analogy_results":
    st.write("Analogy words fetched successfully!")

    col1, int1, col2, int2, col3, int3, col4 = st.columns(7)
    col1.text_input("Word 1", key="word1", value="king", disabled=True)
    int1.write(":")
    col2.text_input("Word 2", key="word2", value="queen", disabled=True)
    int2.write(":::")
    col3.text_input("Word 3", key="word3", value="man", disabled=True)
    int3.write(":")
    col4.text_input("Result", key="result_word", value="woman", disabled=True)

    col1, int1, col2, int2, col3, int3, col4 = st.columns(7)
    col1.text_input("Given Word 1", key="out_analogy_word1", value=st.session_state.analogy_word1, disabled=True)
    int1.write(":")
    col2.text_input("Given Word 2", key="out_analogy_word2", value=st.session_state.analogy_word2, disabled=True)
    int2.write(":::")
    col3.text_input("Given Word 3", key="out_analogy_word3", value=st.session_state.analogy_word3, disabled=True)
    int3.write(":")

    fetched_words = cf.get_analogy_words(
        st.session_state.analogy_word1, st.session_state.analogy_word2, st.session_state.analogy_word3,
          st.session_state.analogy_topn, st.session_state.analogy_model)
    
    col4.text_input("Result", key="out_result_word", value=fetched_words['Word'][1], disabled=True)
    st.write(fetched_words)


    st.button("Back to Home", on_click=back_to_home, key="back_button")
    st.button("Get Similar Words", on_click=go_to_page, args=("similar",), key="similars_button") ##check if it works