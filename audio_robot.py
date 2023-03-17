import pyaudio
import wave
import ftplib

chunk = 1024  # 每次读取的音频块大小
FORMAT = pyaudio.paInt16  # 音频格式
CHANNELS = 1  # 单声道
RATE = 44100  # 采样率
RECORD_SECONDS = 5  # 录制时间

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=chunk)

print("开始录制音频......")

frames = []

for i in range(0, int(RATE / chunk * RECORD_SECONDS)):
    data = stream.read(chunk)
    frames.append(data)

print("录制结束......")

stream.stop_stream()
stream.close()
p.terminate()

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(2),
                channels=CHANNELS,
                rate=RATE,
                output=True)

for data in frames:
    stream.write(data)

stream.stop_stream()
stream.close()
p.terminate()

ftp = ftplib.FTP("ftp.example.com")
ftp.login("
