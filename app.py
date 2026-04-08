import streamlit as st
from data import songs_data

st.title("🎵 Mood-Based Music Suggestor")
st.write("Select your mood and get song recommendations 😄")

mood = st.selectbox("Select your mood:", list(songs_data.keys()))

if st.button("Get Song Recommendations 🎧"):
    songs = songs_data[mood]

    st.subheader(f"Songs for {mood.capitalize()} Mood:")

    for song in songs:
       with st.container():
           col1,col2=st.columns([1,3])
           with col1:
               st.image("https://via.placeholder.com/150", width=100)
           with col2:
               st.markdown(f"song:{song['title']}")
               st.write(f"Artist: {song['artist']}")
    st.divider()   