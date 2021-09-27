from mistyPy.Robot import Robot
from mistyPy.Events import Events
import requests
import json
import time
import base64

if __name__ == "__main__":
    ipAddress = "IP ADDRESS"
    misty = Robot(ipAddress)

    #####  Using API END POINT:  audio/raw/record/start  #####  
    file_to_record = {"FileName": "testRawSound.wav"}
    file = json.dumps(file_to_record, separators=(',', ':')) 
    url = "http://" + ipAddress + "/api/audio/raw/record/start"
    r3_A = requests.post(url, json=file) # Note, POST request for Misty expects a JSON payload
    print(r3_A.status_code)
    # print(r3_A.json())
    time.sleep(1) 
  
    # Stop Recording audio
    url = "http://" + ipAddress + "/api/audio/record/stop"
    r3_B = requests.post(url) 
    print(r3_B.status_code)

    #####  Using API END POINT:  audio/record/start  #####  
    file_to_record = {"FileName": "testSound.wav"}
    file = json.dumps(file_to_record, separators=(',', ':')) 
    url = "http://" + ipAddress + "/api/audio/record/start"
    r3_A = requests.post(url, json=file) # Note, POST request for Misty expects a JSON payload
    print(r3_A.status_code)
    # print(r3_A.json())
    time.sleep(1) 
  
    # Stop Recording audio
    url = "http://" + ipAddress + "/api/audio/record/stop"
    r3_B = requests.post(url) # Note, POST request for Misty expects a JSON payload
    print(r3_B.status_code)

    ####### Get a list of all the audio files 
    url = "http://" + ipAddress + "/api/audio/list"
    r4 = requests.get(url, headers={'Content-Type': 'application/json'})
    print(r4.status_code)
    # print(r4.json()) # displays the list of files as key-value pairs

    ####### Get a specific audio file stored on Misty 
    url = "http://" + ipAddress + "/api/audio?FileName=testRawSound.wav&Base64=True"
    r5 = requests.get(url, headers={'Content-Type': 'application/json'})
    print(r5.status_code)
    print(r5.json()) # This returns testRawSound.wav as a base64 string

    #Convert base64 string to .wav file
    base64string_data = r5.json()
    encoded_audio  = list(base64string_data.values())[0]
    encoded_audio_value = list(encoded_audio.values())[0]
    wav_file = open("testRawSound.wav", "wb")
    decode_string = base64.b64decode(encoded_audio_value)
    wav_file.write(decode_string)

    url = "http://" + ipAddress + "/api/audio?FileName=testSound.wav&Base64=True"
    r5 = requests.get(url, headers={'Content-Type': 'application/json'})
    print(r5.status_code)
    print(r5.json()) # This returns testSound.wav as a base64 string

    #Convert base64 string to .wav file
    base64string_data = r5.json()
    encoded_audio  = list(base64string_data.values())[0]
    encoded_audio_value = list(encoded_audio.values())[0]
    wav_file = open("testSound.wav", "wb")
    decode_string = base64.b64decode(encoded_audio_value)
    wav_file.write(decode_string)
