import speech_recognition as sr
from audio_recorder import record_audio


class SpeechRecognition():
    def __init__(self, path):
        self.r = sr.Recognizer()
        self.path = path
    def record_recognize(self):
        record_audio()
        audio_file = sr.AudioFile(self.path)
        with audio_file as source:
            audio = self.r.record(source)
        text = self.r.recognize_google(audio)
        return text



def main():
    recog = SpeechRecognition('./audio/audio.wav')
    recog.record_recognize()

if __name__ == "__main__":
    main()