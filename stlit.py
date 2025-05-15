import streamlit as st
import pandas as pd
import common_functions as cf

st.title("Similarity Search")
st.write("This is a simple app to fetch similar using pre-trained Word2Vec models.")


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

def go_to_results():
    st.session_state.page = "results"


print(f"1: {st.session_state.page}")
if st.session_state.page == "home":

    st.text_input("Enter a word for similarity search", key="word")#, value=st.session_state.content.get("word", ""))
    st.number_input("Number of similar words", min_value=1, max_value=300, value=10, step=1, key="topn")
    st.radio("Select a model", ("small", "medium"), key="model")

    st.button("Get Similar Words", on_click=go_to_results, key="submit_button")




if st.session_state.page == "results":
    st.write("Similar words fetched successfully!")

    st.text_input("Enter a word for similarity search", key="word")#, value=st.session_state.content.get("word", ""), disabled=True)
    st.number_input("Number of similar words", min_value=1, max_value=300, value=10, step=1, key="topn", disabled=True)
    st.radio("Select a model", ("small", "medium"), key="model", disabled=True)

    fetched_words = cf.get_similar_words(st.session_state.word, st.session_state.topn, st.session_state.model)

    st.write(pd.DataFrame(fetched_words, columns=["Word", "Similarity"]))
    st.button("Back to Home", on_click=back_to_home, key="back_button")