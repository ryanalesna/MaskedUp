#this function will record the microphone for n seconds and then convert the spoken words to text
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    # read the audio data from the default microphone
    r.adjust_for_ambient_noise(source, duration=0.5)
    audio_data = r.record(source, duration=5)
    # convert speech to text
    text = r.recognize_google(audio_data)
    print(text)