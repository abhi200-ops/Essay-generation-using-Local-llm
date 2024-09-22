import requests
import streamlit as st




def get_response(input_text):
    response=requests.post("http://127.0.0.1:8090/essay/invoke",
                           json={'input':{'topic':input_text}})

    return response.json()['output']['content']

def get_ollama_response(input_text):
    response = requests.post("http://127.0.0.1:8090/poem/invoke",
                             json={'input': {'topic': input_text}})

    return response.json()['output']

st.title("langchain api app")
input_text=st.text_input("write an essay on")
input_text1=st.text_input("write a poem on")

if input_text:
    st.write(get_response(input_text))

if input_text1:
    st.write(get_ollama_response(input_text1))

