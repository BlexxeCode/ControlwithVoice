import cv2.cv2
import pyautogui
from cv2 import cv2
import speech_recognition as sr

cap = cv2.VideoCapture

def speech_to_text(recognizer, microphone):
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        result = recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        result = 'Sorry can you say that again?'

    return result


if __name__ == "__main__":
    r = sr.Recognizer()
    mic = sr.Microphone()

    while True:
        print("\nSay something!")
        speak = speech_to_text(r, mic)
        print(f"Response: {speak.title()}.")
        if speak == 'open camera':
            while cap.isOpened():
                success, video_cap = cap.read()
                cv2.imshow("Video", video_cap)

