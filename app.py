"""
File: many-app.py
------------------
More than one philosopher now!  
"""


import streamlit as st
import time
import backend
import pickle



# @st.cache_data
def load_embeddings(philosopher_name):
    """
    Loads in chapter embeddings. 
    """

    if philosopher_name == "Plato":
        with open("embeddings/plato-embeddings.pkl", "rb") as f:
            chapter_embeddings = pickle.load(f)
    elif philosopher_name == "Nietzsche":
        with open("embeddings/nietzsche-embeddings.pkl", "rb") as f:
            chapter_embeddings = pickle.load(f)
    elif philosopher_name == "Kant":
        with open("embeddings/kant-embeddings.pkl", "rb") as f:
            chapter_embeddings = pickle.load(f)
    elif philosopher_name == "gpt":
        return None
    else:
        raise ValueError("Invalid philosopher name")
    
    return chapter_embeddings


def process_input(question, chapter_embeddings, philosopher, open_ai_api_key, temp_):
    """
    Processes input question and constructs answer  
    """
    answer = backend.ask_question(question, chapter_embeddings, philosopher, open_ai_api_key, temperature=temp_)
    return answer


st.header("`PhilGPT`")
st.info("`This is a demo of PhilGPT, a GPT-powered philosopher question and answering bot. It allows you to ask the selected philosopher a question about anything!`")
st.sidebar.write("## Choose your philosopher 💡")
option = st.sidebar.selectbox(
    'Which Philosopher would you like to talk to?',
    ('Plato', 'Nietzsche', 'Kant', 'gpt'))
st.sidebar.write('You selected:', option)
st.sidebar.write("[Source code](https://github.com/rosikand/PhilGPT)")



chapter_embeddings = load_embeddings(option)
open_ai_api_key = st.text_input(label="**OpenAI API Key**:", placeholder=f"Please enter your OpenAI API key")
# assert open_ai_api_key is not "", "Must enter OpenAI API key."
query = st.text_input(label="**Question**:", placeholder=f"What does {option} think...")
temp_ = st.slider('Temperature (Creativity)', 0.0, 0.99, 0.1)

if st.button(f"Ask {option}"):
    with st.spinner('Processing...'):
        time.sleep(1)
        response = process_input(query, chapter_embeddings, option, open_ai_api_key, temp_)
        st.write("**Answer**:", response)

