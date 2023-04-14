import streamlit as st
import moviepy.editor as mp
import speech_recognition as sr
import matplotlib.pyplot as plt

@st.cache_data
def generate_audio(uploaded_file):
    video = mp.VideoFileClip(uploaded_file)
    audio = video.audio
    audio_file = "temp_audio.wav"
    audio.write_audiofile(audio_file)
    st.success('Vídeo convertido em áudio!', icon="✅")
     # Select the language of origin
    language = st.selectbox("Select the language:", ["English", "French", "German", "Spanish"])
    # Convert the language name to a language code
    if language == "English":
        language_code = "en-US"
    elif language == "French":
        language_code = "fr-FR"
    elif language == "German":
        language_code = "de-DE"
    elif language == "Spanish":
        language_code = "es-ES"
    return audio_file, language

@st.cache_data
def transcribe_audio(audio_file, language):
    # Create a new recognizer object
    r = sr.Recognizer()
    # Open the audio file and read its contents into memory
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)
    # Transcribe the audio file using Google Speech Recognition
    try:
        text = r.recognize_google(audio, language=language)
        st.success('Áudio convertido em texto!', icon="✅")
    except sr.UnknownValueError:
        text = "Unable to transcribe audio"
    # Return the transcribed text
    return text

# Set up the Streamlit app
st.set_page_config(page_title="BookTalker: 📺➡📖", page_icon=":guardsman:", layout="wide")
st.title("Convert your talks into best-sellers!")

# Add a file uploader to the app
uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "mov"])
if st.button("Run"):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Use moviepy to extract audio from the video
        generate_audio(uploaded_file)
        # Use Google Speech Recognition API to convert audio to text
        transcribe_audio(audio_file, language)
        if audio_file is not None:
                text = transcribe_audio(audio_file, language=language_code)
                txt = st.text_area('Transcription', text)
        else:
            st.error('Some error with the audio', icon="🚨")
    else:
        st.error('Some error with the video', icon="🚨") 
