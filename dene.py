import soundfile as sf
import sounddevice as sd


samplerate = 16000  
duration = 1 # seconds
filename = 'right.wav'
print("start")
mydata = sd.rec(int(samplerate * duration), samplerate=samplerate,
    channels=1, blocking=True)
print("end")
sd.wait()
sf.write(filename, mydata, samplerate)