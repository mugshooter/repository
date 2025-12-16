import pyttsx3

def text_to_speech_pyttsx3(text, filename):
    engine = pyttsx3.init()
    engine.save_to_file(text, filename)
    engine.runAndWait()

if __name__ == "__main__":
    text = "Привет, это тестовая программа, написанная при помощи pyttsx3,для сравнения методов синтеза речи"
    filename = r"C:\Users\gnevn\OneDrive\Рабочий стол\учеба\РГПУ\Технологии комп. моделирования\Курсовая\аудио\output_pyttsx3.wav"
    text_to_speech_pyttsx3(text, filename)
    
    