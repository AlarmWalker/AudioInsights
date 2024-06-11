import wave
import sys
import keyboard
import pyaudio


# record system audio until 'q' is pressed
def record_audio(output_filename="output.wav", stop_key="q"):

    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024

    audio = pyaudio.PyAudio()

    stream = audio.open(
        format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK
    )
    print("Recording... Press '{}' to stop.".format(stop_key))

    frames = []

    try:
        while not keyboard.is_pressed(stop_key):
            data = stream.read(CHUNK)
            frames.append(data)
    except KeyboardInterrupt:
        print("Recording interrupted")
    finally:
        print("Finished recording")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded audio
    wf = wave.open(output_filename, "wb")
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b"".join(frames))
    wf.close()
    print(f"Audio saved to {output_filename}")


if __name__ == "__main__":
    record_audio()
