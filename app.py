import streamlit as st
from textblob import TextBlob

# Initialize session state for history
if "history" not in st.session_state:
    st.session_state.history = []

# Emoji styles
emoji_styles = {
    "Classic": {
        "very_positive": "🤩",
        "positive": "😊",
        "neutral": "😐",
        "negative": "☹️",
        "very_negative": "😡",
    },
    "Cute": {
        "very_positive": "✨🐥",
        "positive": "🌸😊",
        "neutral": "🍃😐",
        "negative": "💧😕",
        "very_negative": "💔😭",
    },
    "Sarcastic": {
        "very_positive": "🙄🎉",
        "positive": "😉",
        "neutral": "😏",
        "negative": "🤦",
        "very_negative": "🤬",
    }
}

# Function to analyze sentiment and choose emoji
def add_emoji(text, style):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    confidence = round(abs(polarity), 2)

    if polarity > 0.5:
        emoji = emoji_styles[style]["very_positive"]
    elif polarity > 0.1:
        emoji = emoji_styles[style]["positive"]
    elif polarity < -0.5:
        emoji = emoji_styles[style]["very_negative"]
    elif polarity < -0.1:
        emoji = emoji_styles[style]["negative"]
    else:
        emoji = emoji_styles[style]["neutral"]

    return f"{text} {emoji} (score: {polarity:.2f})"

# Streamlit app
st.set_page_config(page_title="Emoji Sentiment Translator", page_icon="✨")
st.title("📝 Emoji Sentiment Translator")
st.write("Type text, choose emoji style, and see how it feels! 🌈")

style = st.selectbox("Choose your emoji style:", list(emoji_styles.keys()))

user_input = st.text_area("Enter your text here:")

if st.button("Translate"):
    if user_input.strip() != "":
        result = add_emoji(user_input, style)
        st.success(result)
        # Save to history
        st.session_state.history.insert(0, result)
    else:
        st.warning("Please enter some text first!")

# Show history
if st.session_state.history:
    st.subheader("📝 Recent Translations")
    for item in st.session_state.history[:5]:
        st.write(f"- {item}")
