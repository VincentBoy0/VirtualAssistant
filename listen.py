import speech_recognition

def audioToText(myLang = "en"):
    robot_ear = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        #print("Robot: I'm hearing")
        #print("Robot: ...")
        audio = robot_ear.record(mic, duration=5)
    try:
        text = robot_ear.recognize_google(audio, language = myLang)
    except:
        text = ""    
    return text