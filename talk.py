# import text to speech
import pyttsx3

# create a function to talk with a parameter for the text
def talk(text):
    # initialise a talk engine
    engine = pyttsx3.init()
    # say what is in the text parameter
    engine.say(text)
    engine.runAndWait()
