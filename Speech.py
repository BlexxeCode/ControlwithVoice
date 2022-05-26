import pyautogui
import speech_recognition as sr

r = sr.Recognizer()

mic = sr.Microphone()


while True:
    print("\nSay something!")
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    print(r.recognize_google(audio))
    if r.recognize_google(audio) == 'hello':
        pyautogui.press('win')
    if r.recognize_google(audio) == 'quit':
        break
