import speech_recognition
import win32com.client
import webbrowser
import datetime
import pyttsx3
speaker=win32com.client.Dispatch("SAPI.SpVoice")
recognizer= speech_recognition.Recognizer()
speaker.Speak("Hello Sir!, I am Vikram-1. How may I help You?")
def command():
    print("Listening.....")
    try:
        with speech_recognition.Microphone() as mic: 
            recognizer.adjust_for_ambient_noise(mic,duration=0.05)
            audio=recognizer.listen(mic)

            text=recognizer.recognize_google(audio)
            text=text.lower()
            return text
            
            print(f"Recognized....{text}")
    except speech_recognition.exceptions.UnknownValueError:
        speaker.Speak("Didn't get it , Can you, Please Repeat!")
        print("Can you, Please Repeat!")
        command()
    
while True:
    query=command()
    if "youtube" in query:
        speaker.Speak("Opening Youtube for You, Sir.......")
        webbrowser.open("https://youtube.com")
    if "google" in query:
            speaker.Speak("Opening Google for You, Sir.......")
            webbrowser.open("https://google.com")
    if "mail" in query:
            speaker.Speak("Opening Mail for You, Sir.......")
            webbrowser.open("https://mail.com")

    if "time" in query:
        h=datetime.datetime.now().strftime("%H")
        m=datetime.datetime.now().strftime("%M")
        s=datetime.datetime.now().strftime("%S")

        speaker.Speak("Time is %s ours"%h )
        speaker.Speak(" %s Minutes"%m)
        speaker.Speak("and %s Seconds and going on , tik tik tik tik tik....."%s)
        print("Time is ",h,"Hours",m,"Minutes and",s,"Seconds")

   
    

   
    