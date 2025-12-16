import subprocess

def text_to_speech_espeak(text, filename):
    subprocess.run(["espeak", "-v", "en", "-w", filename, text])

if __name__ == "__main__":
    text = "Hi, this is a test program written using eSpeak to compare speech synthesis methods"
    filename = r"C:\Users\gnevn\OneDrive\Рабочий стол\учеба\РГПУ\Технологии комп. моделирования\Курсовая\аудио\output_espeak.wav"
    text_to_speech_espeak(text, filename)

