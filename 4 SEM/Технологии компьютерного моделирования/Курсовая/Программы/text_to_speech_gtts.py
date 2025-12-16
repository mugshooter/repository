from gtts import gTTS

def text_to_speech_gtts(text, filename, language='ru'):
    tts = gTTS(text=text, lang=language)
    tts.save(filename)

if __name__ == "__main__":
    text = "Привет, это тестовая программа, написанная при помощи gTTS,для сравнения методов синтеза речи"
    filename = r"C:\Users\gnevn\OneDrive\Рабочий стол\учеба\РГПУ\Технологии комп. моделирования\Курсовая\аудио\output_gtts.mp3"
    text_to_speech_gtts(text, filename)

