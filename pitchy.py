import aubio
import numpy as num
import pyaudio
import sys
import json
import keyboard

BUFFER_SIZE             = 2048
CHANNELS                = 1
FORMAT                  = pyaudio.paFloat32
METHOD                  = "default"
SAMPLE_RATE             = 44100
HOP_SIZE                = BUFFER_SIZE//2
PERIOD_SIZE_IN_FRAME    = HOP_SIZE

def main(args):
    pA = pyaudio.PyAudio()
   
    mic = pA.open(format=FORMAT, channels=CHANNELS,
        rate=SAMPLE_RATE, input=True,
        frames_per_buffer=PERIOD_SIZE_IN_FRAME)

    pDetection = aubio.pitch(METHOD, BUFFER_SIZE,
        HOP_SIZE, SAMPLE_RATE)
   
    pDetection.set_unit("Hz")
 
    pDetection.set_silence(-40)
    config_data = json.load(open("config.json"))
    
    key_map = {}
    for bind in config_data["key_map"]:
        #print(bind)
        key_map[bind["key"]] = [bind["min"], bind["max"]]
    
    print("Configured input map:")
    for key, val in key_map.items():
        print(key, val)
        

    while True:
        data = mic.read(PERIOD_SIZE_IN_FRAME)
        samples = num.fromstring(data,
            dtype=aubio.float_type)
        pitch = pDetection(samples)[0]

        volume = num.sum(samples**2)/len(samples)
        volume = "{:6f}".format(volume)

        print(str(pitch) + " " + str(volume))

        for key, val in key_map.items():
            if pitch > val[0] and pitch < val[1]:
                print(key)
                keyboard.press(key)
            else:
                keyboard.release(key)

if __name__ == "__main__": main(sys.argv)
