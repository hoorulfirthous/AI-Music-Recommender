import streamlit as st
from data import songs_data
from recommender import detect_mood, recommend_songs

st.title("🎵 Mood-Based Music Suggestor")
st.write("Select your mood and get song recommendations 😄")

user_input=st.text_input("how's your day")

if st.button("Get Song Recommendations 🎧"):
    if user_input:
        mood = detect_mood(user_input)

        st.success(f"Detected Mood: {mood.capitalize()} 💡")

        songs = recommend_songs(mood)

        for song in songs:
            with st.container():
                col1,col2=st.columns([1,3])
                with col1:
                    st.image("https://via.placeholder.com/150", width=100)
                with col2:
                    st.markdown(f"song:{song['title']}")
                    st.write(f"Artist: {song['artist']}")

                    query = f"{song['title']} {song['artist']}"
                    youtube_url= f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"

                    st.markdown(f"[Watch on YouTube]({youtube_url})")
        st.divider()   