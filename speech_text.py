import speech_recognition as sr
def speech_recog():
    r=sr.Recognizer()
    mic=sr.Microphone()

    while True:
        with mic as source:
            print("speek.....")
            audio=r.listen(source)

            try:
                text=r.recognize_google(audio)
                print(text)
            except:
                print("didn't hear anything pls repeat....")
speech_recog()