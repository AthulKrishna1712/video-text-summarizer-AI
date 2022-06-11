import speech_recognition as sr
AUDIO_FILE=("D:\python\Manasellam.wav")
r=sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio=r.record(source)
try:
    print("audio file contains:\n"+r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("not reco")
except sr.RequestError:
    print("not reco 2")