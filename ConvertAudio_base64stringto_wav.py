from mistyPy.Robot import Robot
from mistyPy.Events import Events
import requests
import json
import time
import base64

if __name__ == "__main__":
    ipAddress = "IP_ADDRESS"
    misty = Robot(ipAddress)

    #### Get the list of all the audio files stored in Misty
    url = "http://" + ipAddress + "/api/audio/list"
    r4 = requests.get(url, headers={'Content-Type': 'application/json'})
    print(r4.status_code)
    # print(r4.json()) # diplays the list of files as key-value pairs

    #### Get a specific audio file stored on Misty
    url = "http://" + ipAddress + "/api/audio?FileName=deleteThis.wav&Base64=True"
    r5 = requests.get(url, headers={'Content-Type': 'application/json'})
    print(r5.status_code)
    #print(r5.json()) # diplays the list of files as key-value pairs
    
    #### Misty returns an audio file as base64 string. Convert it to .wav format
    base64string_data = r5.json()
    encoded_audio  = list(base64string_data.values())[0]
    encoded_audio_value = list(encoded_audio.values())[0]
    wav_file = open("temp.wav", "wb")
    decode_string = base64.b64decode(encoded_audio_value)
    wav_file.write(decode_string)









