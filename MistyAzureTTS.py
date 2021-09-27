from mistyPy.Robot import Robot
from mistyPy.Events import Events
import matplotlib.pyplot as plt 
import numpy as np
import base64
import requests
import json
import time
import wave
from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer, SpeechSynthesisOutputFormat
from azure.cognitiveservices.speech.audio import AudioOutputConfig 

if __name__ == "__main__":
    ipAddress = "IP ADDRESS"
    misty = Robot(ipAddress)

    speech_key, service_region = "KEY", "REGION"
    speech_config = SpeechConfig(subscription=speech_key, region=service_region)

    audio_config = AudioOutputConfig(filename="file.wav")

    # Creates a speech synthesizer using the default speaker as audio output.
    speech_synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)


    #print("Type some text that you want to speak...")
    #text = input()
    speech_synthesizer.speak_text_async("Write test to file.") # can change text

    enc = base64.b64encode(open("file.wav", "rb").read())
    eenc = enc.decode("utf-8")

    parameters = {"FileName": "file.wav", "Data": eenc, "ImmediatelyApply": True, "OverwriteExisting": True}
    #text = json.dumps(parameters, separators=(',', ':')) #Convert to JSON (optional)
    url = "http://" + ipAddress + "/api/audio"
    Qr1 = requests.post(url, json=parameters) # Note, POST request for Misty expects a JSON payload
    print(Qr1)

