import pyttsx3

tts = pyttsx3.init()

voices = tts.getProperty('voices')
tts.setProperty('voice', voices[0].id)
tts.say('Isaac you are very late')

tts.runAndWait()