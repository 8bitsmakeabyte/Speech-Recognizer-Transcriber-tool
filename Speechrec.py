import speech_recognition as sr

r = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            print("Hello, say something: ")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

            text = r.recognize_google(audio)
            text = text.lower()
            print(f"Transcribed text: {text}")

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")


    except Exception as e:

        print(f"An error occurred: {e}")
        continue
