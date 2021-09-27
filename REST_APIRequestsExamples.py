# This file provides examples of various REST API methods to communicate with Misty (such as GET, POST, DELETE)
# Make sure to enter the appropriate IP ADDRESS before running the code 

from mistyPy.Robot import Robot
from mistyPy.Events import Events
import requests
import json
import time

if __name__ == "__main__":
    ipAddress = "IP ADDRESS"
    misty = Robot(ipAddress)

    #### Example1: POST Method (with parameters) --- Display a TEXT on Misty's screen: Endpoint: POST <robot-ip-address>/api/text/display
    textToDisplay = {"Text": "Hello World"}
    text = json.dumps(textToDisplay, separators=(',', ':')) #Convert to JSON
    url = "http://" + ipAddress + "/api/text/display"
    r1 = requests.post(url, json=textToDisplay) # Note, POST request for Misty expects a JSON payload
    print(r1.status_code) # The staus code of 200 means, the request was successful and a text "Hello World" is dispalyed on the MIsty's screen
    #print(r1.json())

    #### Example2: POST methods with and without parameters --- Drive Misty at a certain speed, wait for 5 seconds and then stop
    # Example2A: POST Method (with parameters) -- Drive Misty at a certian speed (set to 5 m/s in the example below)
    MistyVelocity = {"LinearVelocity": 5, "AngularVelocity": 0}
    velocity = json.dumps(MistyVelocity, separators=(',', ':')) 
    url = "http://" + ipAddress + "/api/drive"
    r2_A = requests.post(url, json=velocity) 
    print(r2_A.status_code)
    # print(r2_A.json())

    time.sleep(5)  # Wait for 5 seconds 

    # Eample2B: POST Method (without parameters) -- Stop driving Misty
    url = "http://" + ipAddress + "/api/drive/stop"
    r2_B = requests.post(url) 
    print(r2_B.status_code)

    #### Example3: POST Method with and without parameters --- Start Recording Audio for 1 second and then stop recording
    # Example3A: POST Method (with parameters) -- Start recording audio and save to a file with the provided filename
    file_to_record = {"FileName": "TroyCenter.wav"}
    file = json.dumps(file_to_record, separators=(',', ':')) 
    url = "http://" + ipAddress + "/api/audio/record/start"
    r3_A = requests.post(url, json=file) 
    print(r3_A.status_code)
    # print(r3_A.json())

    time.sleep(1)  # wait for 2 seconds

    # Eample3B: POST Method (without parameters) -- Stop Recording audio
    url = "http://" + ipAddress + "/api/audio/record/stop"
    r3_B = requests.post(url) 
    print(r3_B.status_code)
    # print(r3_B.json())

    #### Example4: GET Method (without parameters) -- get the list of all the audio files stored in Misty
    url = "http://" + ipAddress + "/api/audio/list"
    r4 = requests.get(url, headers={'Content-Type': 'application/json'})
    print(r4.status_code)
    print(r4.json()) # diplays the list of audio files as key-value pairs

    #### Example5: GET Method (with parameters) -- get a specific audio file stored on Misty
    url = "http://" + ipAddress + "/api/audio?FileName=TroyCenter.wav&Base64=True"
    r5 = requests.get(url, headers={'Content-Type': 'application/json'})
    print(r5.status_code)
    #print(r5.json()) # this returns the audio file as a base64 string. This can be later converted to a .wav file as needed

    #### Example6: DELETE Method (with parameters) -- delete a specific audio file
    file_to_delete = {"FileName": "TroyCenter.wav"}
    file_ = json.dumps(file_to_delete, separators=(',', ':')) 
    url = "http://" + ipAddress + "/api/audio"
    r6 = requests.delete(url, json=file_) 
    print(r6.status_code)
