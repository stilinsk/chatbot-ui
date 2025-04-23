import os
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain.chat_models import ChatOpenAI

def get_openai_response(question):
    llm = ChatOpenAI(
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        model="gpt-3.5-turbo",
        temperature=0.5
    )
    response = llm.invoke(question)
    return response.content  # .content gives the actual text

# Streamlit UI
st.set_page_config(page_title="GenAI", page_icon=":robot_face:")
st.header("GenAIbot")

input_text = st.text_input("Input:", key="input")

submit = st.button("Ask the Question")

if submit and input_text:
    response = get_openai_response(input_text)
    st.subheader("The response is:")
    st.write(response)
