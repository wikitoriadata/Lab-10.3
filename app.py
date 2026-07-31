import streamlit as st
import pandas as pd
import joblib
import utils

st.set_page_config(page_title="Custom Sentiment App", page_icon="🎨")

def run():
    model = joblib.load(open('model.joblib', 'rb'))

    # Personalized and colored header
    st.markdown("<h1 style='color: #ff4b4b;'>✨ My Personalized Sentiment Analysis App</h1>", unsafe_allow_html=True)
    st.write("Welcome! Built as part of Lab-10.3 to analyze text sentiment with a personal touch.")
    st.markdown("---")
    
    userinput = st.text_input('Enter text below, then click the Predict button.', placeholder='Type something here...')
    st.text("")
    
    if st.button("Predict"):
        if userinput.strip() == "":
            st.warning("Please enter some text before predicting.")
        else:
            predicted_sentiment = model.predict(pd.Series([userinput]))[0]
            if predicted_sentiment == 1:
                output = 'positive 👍'
                sentiment = f'Predicted sentiment of "{userinput}" is {output}.'
                st.success(sentiment)
            else:
                output = 'negative 👎'
                sentiment = f'Predicted sentiment of "{userinput}" is {output}.'
                st.error(sentiment)

if __name__ == "__main__":
    run()
