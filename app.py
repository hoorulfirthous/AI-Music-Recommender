import streamlit as st
from data import songs_data
from recommender import detect_mood, recommend_songs
from streamlit_mic_recorder import mic_recorder
import speech_recognition as sr
import io
import whisper
import tempfile


st.title("🎵 Mood-Based Music Suggestor")
st.write("Select your mood and get song recommendations 😄")
model = whisper.load_model("base")

user_input=st.text_input("how's your day")

st.subheader("or speak your mood 🎤")
audio=mic_recorder(start_prompt="start recording",stop_prompt="stop recording")

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
    # 🎤 Voice Input Processing
    
    if audio is not None:
        st.audio(audio["bytes"])
        # Save audio temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".webm") as temp_audio:
            temp_audio.write(audio["bytes"])
            temp_audio_path = temp_audio.name

        # 🔥 Whisper transcription
        result = model.transcribe(temp_audio_path)
        text = result["text"]

        st.success(f"You said: {text}")

        mood = detect_mood(text)
        st.success(f"Detected Mood: {mood}")

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