import streamlit as st
import speech_recognition as sr
from textblob import TextBlob

# Function to record and recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            st.success("Recognized Text: " + text)
            return text
        except sr.UnknownValueError:
            st.error("Could not understand the audio")
        except sr.RequestError:
            st.error("Could not request results; check your network connection")

# Function to analyze sentiment
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    return sentiment

# Streamlit interface
st.title("Live Speech-to-Text Conversation with Sentiment Analysis")

if st.button("Record Voice"):
    text = recognize_speech()
    if text:
        sentiment = analyze_sentiment(text)
        st.write("Sentiment Analysis:")
        st.write(f"Polarity: {sentiment.polarity}, Subjectivity: {sentiment.subjectivity}")

