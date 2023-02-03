import pyaudio
import wave

def record_audio():
    CHUNK = 1024  # Number of audio frames per buffer
    FORMAT = pyaudio.paInt16  # Audio sample format (16-bit int in this case)
    CHANNELS = 2  # Number of audio channels (1 for mono, 2 for stereo)
    RATE = 44100  # Audio sample rate (in samples per second)
    RECORD_SECONDS = 3  # Number of seconds to record
    WAVE_OUTPUT_FILENAME = "./audio/audio.wav"  # File name for the recorded audio

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* Recording audio...")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* Done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()