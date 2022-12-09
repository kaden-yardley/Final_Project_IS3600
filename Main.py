import streamlit as st
from model import GeneralModel
from secrets_1 import access_key, secret_access_key
import boto3
import os


def app():

    # Creating an object of prediction service
    pred = GeneralModel()
    userTemp = st.slider('Complexity?', 1, 50, 1) * .02
    userLength = st.slider('Length?', 1, 25, 1) * 100
    api_key = st.sidebar.text_input("APIkey", type="password")

    # Using the streamlit cache
    @st.cache
    def process_prompt(input):

        input2=input.strip()
        return pred.model_prediction(input2, userTemp, userLength, api_key=api_key)
 

    if api_key:

        # Setting up the Title
        st.title("Write a poem based on these words")

        # st.write("---")

        s_example = "Birds, flowers, love, sun"
        input = st.text_area(
            "Use the example below or input your own text in English",
            value=s_example,
            max_chars=150,
            height=100,
        )

        if st.button("Submit"):
            with st.spinner(text="In progress"):
                report_text = process_prompt(input)
                with open(str(input), 'w') as f:
                    f.write(report_text)

                client = boto3.client('s3', aws_access_key_id = access_key, aws_secret_access_key = secret_access_key)

                upload_file_bucket = 'kadenfinalproject'
                upload_file_key = str(input) + ".txt"
                client.upload_file(str(input), upload_file_bucket, upload_file_key)
                st.markdown(report_text)
    else:
        st.error("🔑 Please enter API Key")
