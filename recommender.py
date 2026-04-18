from data import songs_data

def detect_mood(user_input):
    text = user_input.lower()

    mood_keywords = {
        "happy": ["happy", "good", "great", "awesome", "joy"],
        "sad": ["sad", "lonely", "cry", "depressed", "hurt"],
        "angry": ["angry", "mad", "frustrated", "annoyed"],
        "excited": ["excited", "party", "celebration", "thrilled"],
        "relaxed": ["tired", "stress", "calm", "relax", "peace"],
        "love": ["love", "romantic", "crush", "heart", "miss","lovely"],
        "motivation": ["motivate","frustrated" ,"inspire", "success", "goal", "win","motivational"],
        "attitude": ["attitude","frustrated", "swagger", "mass", "power", "bossy","fire"]
    }

    # 🔍 Check all moods
    mood_score = {mood: 0 for mood in mood_keywords}

    # 🔍 Count matches
    for mood, keywords in mood_keywords.items():
        for word in keywords:
            if word in text:
                mood_score[mood] += 1

    # 🏆 Get best mood
    best_mood = max(mood_score, key=mood_score.get)

    # If no match at all
    if mood_score[best_mood] == 0:
        return "happy"

    return best_mood

def recommend_songs(mood):
    return songs_data.get(mood, [])