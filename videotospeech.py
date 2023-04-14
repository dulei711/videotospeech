import streamlit as st
import moviepy.editor as mp
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


def generate_wordcloud(audio_text):
    # Create a WordCloud object
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(width = 800, height = 800, background_color ='white', stopwords = stopwords, min_font_size = 10).generate(audio_text)
    
    # Plot the WordCloud image
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    
    # Return the plot as an image
    return plt


# Set up the Streamlit app
st.set_page_config(page_title="Video to WordCloud", page_icon=":guardsman:", layout="wide")
st.title("Convert a video to a WordCloud")

# Add a file uploader to the app
uploaded_file = st.file_uploader("Choose an MP4 video file", type=["mp4", "mov"], max_upload_size=3000))

# Check if a file has been uploaded
if uploaded_file is not None:
    # Use moviepy to extract audio from the video
    video = mp.VideoFileClip(uploaded_file)
    audio = video.audio
    audio_file = "temp_audio.wav"
    audio.write_audiofile(audio_file)

    # Use Google Speech Recognition API to convert audio to text
    audio_text = "TODO: use a speech-to-text API to get the text from the audio file"

    # Generate the WordCloud and display it in Streamlit
    st.pyplot(generate_wordcloud(audio_text))
