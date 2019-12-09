import pyaudio # from http://people.csail.mit.edu/hubert/pyaudio/
import numpy   # from http://numpy.scipy.org/
import audioop
import sys
import math
import struct

chunk      = 2**11 # Change if too fast/slow, never less than 2**11
scale      = 50    # Change if too dim/bright
exponent   = 5     # Change if too little/too much difference between loud and quiet sounds
samplerate = 44100

def calculate_levels(data, chunk, samplerate):
    # Use FFT to calculate volume for each frequency
    global MAX
 
    # Convert raw sound data to Numpy array
    fmt = "%dH"%(len(data)/2)
    data2 = struct.unpack(fmt, data)
    data2 = numpy.array(data2, dtype='h')
 
    # Apply FFT
    fourier = numpy.fft.fft(data2)
    ffty = numpy.abs(fourier[0:int(len(fourier)/2]))/1000
    ffty1=ffty[:int(len(ffty)/2)]
    ffty2=ffty[int(len(ffty)/2)::]+2
    ffty2=ffty2[::-1]
    ffty=ffty1+ffty2
    ffty=numpy.log(ffty)-2
   
    fourier = list(ffty)[4:-4]
    fourier = fourier[:int(len(fourier)/2)]
   
    size = len(fourier)
 
    # Add up for 6 lights
    levels = [sum(fourier[i:int((i+size/6))]) for i in xrange(0, size, size/6)][:6]
   
    return levels

CHUNK = 4096 # number of data points to read at a time
RATE = 44100 # time resolution of the recording device (Hz)

p=pyaudio.PyAudio() # start the PyAudio class
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK) #uses default input device

data  = stream.read(chunk)
 
# Do FFT
levels = calculate_levels(data, chunk, samplerate)

# Make it look better and send to serial
for level in levels:
    level = max(min(level / scale, 1.0), 0.0)
    level = level**exponent
    level = int(level * 255)

print(levels)

# close the stream gracefully
stream.stop_stream()
stream.close()
p.terminate()