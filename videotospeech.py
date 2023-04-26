# importing libraries 
import numpy as np
import matplotlib.pyplot as plt
import moviepy.editor as mp
import speech_recognition as sr 
import os 
from os import path
from pydub import AudioSegment
from pydub.silence import split_on_silence
from pathlib import Path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

def get_large_audio_transcription(path, lang):
    sound = AudioSegment.from_wav(path)  
    chunks = split_on_silence(sound, min_silence_len = 500, silence_thresh = sound.dBFS-14, keep_silence=500)
    folder_name = "audio-chunks"
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    for i, audio_chunk in enumerate(chunks, start=1):
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            try:
                text = r.recognize_google(audio_data=audio_listened, language=lang)
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                print(chunk_filename, ":", text)
                whole_text += text
    return whole_text

st.title("VideoToSpeech")
video_file = st.file_uploader("Choose a file", type=['mov', 'mp4'])
if video_file is not None:
    lang = st.radio("What's the language?", ('en-US', 'pt-BR'))
    if lang:
        if st.button("Run"):
            clip = mp.VideoFileClip(video_file).subclip(0)
            clip.audio.write_audiofile("theaudio_part.wav")
            r = sr.Recognizer()
            path = "/content/theaudio_part.wav"
            text = get_large_audio_transcription(path, lang)
            st.write(text)
