import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import re

# init pyttsx
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")


engine.setProperty('voice', voices[0].id)  # 1 for female and 0 for male voice




def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Zuhören...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Verstehen...")
        query = r.recognize_google(audio, language='de-DE')
        print("Ich habe verstanden:" + query + "\n")
    except Exception as e:
        print(e)
        speak("Ich habe dich leider nicht verstanden")
        return "None"
    return query

def prozentzahl():
    faktor = re.findall(r'\d+', query)
    faktor = float(faktor[0])/100
    return faktor



if __name__ == '__main__':

    speak("Guten Tag, Sona wurde aktiviert! ")
    speak("Wie kann ich dir helfen?")
    while True:
        volume = engine.getProperty('volume')
        query = take_command().lower()
        if 'wikipedia' in query:
            speak("Durchsuche Wikipedia")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=2)
            speak("laut Wikipedia")
            speak(results)
        elif 'wer bist du' in query:
            speak("Ich bin der Sprachasisstent Sona, ich kann verschiedene Befehle ausführen. Falls du einige Beispiele hören möchtest, sage: 'Befehle'")
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif 'öffne google' in query:
            speak("opening google")
            webbrowser.open("google.com")
        elif 'öffne github' in query:
            speak("opening github")
            webbrowser.open("github.com")
        elif 'öffne stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")
        elif 'öffne spotify' in query:
            speak("öffne spotify")
            webbrowser.open("spotify.com")
        elif 'öffne whatsapp' in query:
            speak("öffne whatsapp")
            loc = "C:\\Users\\jaspr\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(loc)
        elif 'spiele musik' in query:
            speak("opening music")
            webbrowser.open("spotify.com")
        elif 'local disk d' in query:
            speak("opening local disk D")
            webbrowser.open("D://")
        elif 'local disk c' in query:
            speak("opening local disk C")
            webbrowser.open("C://")
        elif 'local disk e' in query:
            speak("opening local disk E")
            webbrowser.open("E://")
        elif query =='lautstärke':
            speak("Die Lautstärke ist derzeit auf" + str(int(volume*100)) + "% eingestellt")
        elif 'lauter' in query:
            if volume == 1.0:
                speak("Die Lautsstärke ist bereits bei 100%")
            else:
                engine.setProperty('volume', volume+0.25)
                speak("Die Lautstärke wurde auf" + str(int((volume+0.25)*100)) + "% erhöht")
        elif 'leiser' in query:
            engine.setProperty('volume', volume-0.25)
            speak("Die Lautstärke wurde auf" + str(int((volume-0.25)*100)) + "% verringert")
        elif 'erhöhe die lautstärke um' in query:
            faktor = prozentzahl()
            if volume + faktor < 1.0:
                engine.setProperty('volume', volume+faktor)
                speak("Die Lautstärke wurde auf" + str(int((volume+faktor)*100)) + "% erhöht")
            elif volume == 1.0:
                speak("Die Lautsstärke ist bereits bei 100%")
            else:
                engine.setProperty('volume', 1.0)
                speak("Die Lautstärke wurde auf das Maximum erhöht")
        elif 'verringere die lautstärke um' in query:
            faktor = prozentzahl()
            if volume - faktor > 0.0:
                engine.setProperty('volume', volume-faktor)
                speak("Die Lautstärke wurde auf" + str(int((volume-faktor)*100)) + "% verringert")
            else:
                speak("Ich schalte mich nun stumm")
                engine.setProperty('volume', 0.0)
        elif 'setze die Lautstärke auf' in query:
            faktor = prozentzahl()
            engine.setProperty('volume', faktor)
            print(faktor)
            speak("Die Lautstärke beträgt nun" + str(int((faktor)*100)) + "%") 
        elif 'stop' in query:
            speak("auf wiedersehen")
            exit(0)
