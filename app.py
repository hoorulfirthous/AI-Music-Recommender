import streamlit as st
from data import songs_data
from recommender import detect_mood, recommend_songs


try:
    from streamlit_mic_recorder import mic_recorder
    import whisper
    import tempfile
    voice_enabled = True
except:
    voice_enabled = False


st.set_page_config(
    page_title="AuraBeats AI 🎧",
    page_icon="🎧",
    layout="wide"
)

st.title("🎧❤️‍🔥 AuraBeats AI")
st.caption("Feel the vibe. Play your aura. 🎶")


if voice_enabled:
    model = whisper.load_model("base")


user_input = st.text_input("💬 How's your day?")


if voice_enabled:
    st.subheader("🎤 Speak your mood")
    audio = mic_recorder(
        start_prompt="Start Recording",
        stop_prompt="Stop Recording"
    )
else:
    st.warning("🎤 Voice feature not available in cloud version")
    audio = None


if st.button("Get Song Recommendations 🎧"):
    if user_input:
        mood = detect_mood(user_input)
        st.success(f"Detected Mood: {mood.capitalize()} 💡")

        songs = recommend_songs(mood)

        for song in songs:
            with st.container():
                col1, col2 = st.columns([1, 3])

                with col1:
                    st.image("https://via.placeholder.com/150", width=100)

                with col2:
                    st.markdown(f"### 🎵 {song['title']}")
                    st.write(f"👤 {song['artist']}")

                    query = f"{song['title']} {song['artist']}"
                    youtube_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"

                    st.markdown(f"[▶️ Watch on YouTube]({youtube_url})")

        st.divider()


if voice_enabled and audio is not None:
    st.audio(audio["bytes"])

    # Save temp audio file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".webm") as temp_audio:
        temp_audio.write(audio["bytes"])
        temp_audio_path = temp_audio.name

    # Whisper transcription
    result = model.transcribe(temp_audio_path)
    text = result["text"]

    st.success(f"You said: {text}")

    mood = detect_mood(text)
    st.success(f"Detected Mood: {mood}")

    songs = recommend_songs(mood)

    for song in songs:
        with st.container():
            col1, col2 = st.columns([1, 3])

            with col1:
                st.image("https://via.placeholder.com/150", width=100)

            with col2:
                st.markdown(f"### 🎵 {song['title']}")
                st.write(f"👤 {song['artist']}")

                query = f"{song['title']} {song['artist']}"
                youtube_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"

                st.markdown(f"[▶️ Watch on YouTube]({youtube_url})")

    st.divider()