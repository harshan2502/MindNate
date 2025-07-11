import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


st.set_page_config(page_title="MindMate_Mental Helath Monitor")
st.title("Mimdmate - Daily Menatl Health CHeck-in")
st.markdown("Hi there! How are you feeling today? Just type a few lines and I’ll try to understand your mood.")
userInput=st.text_area("Write how you're feeling:")
if st.button("Analyze Mood"):
    if userInput.strip()!="":
        analyzer=SentimentIntensityAnalyzer()
        score=analyzer.polarity_scores(userInput)
        sentiscore=score['compound']
        if sentiscore>0.2:
            mood = "😊 Positive"
            suggestion = "Keep going! You’re doing great."
        elif sentiscore < -0.2:
            mood = "😟 Negative"
            suggestion = "It’s okay to have rough days. Try taking a short walk or talk to someone."
        else:
            mood = "😐 Neutral"
            suggestion = "Maybe a deep breath or a small break will help."

        
       
        st.subheader("Mood analysis")
        st.write(f"**Detected Mood:**{mood}")
        st.info(suggestion)
else:
    st.warning("please write something about how you are feeling!!") 
