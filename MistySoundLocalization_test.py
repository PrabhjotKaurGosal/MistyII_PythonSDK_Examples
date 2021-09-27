# This code starts recording audio, registers to the 'SourceTrackDataMessage' event to get the sound localization data back from Misty

from mistyPy.Robot import Robot
from mistyPy.Events import Events
from mistyPy.EventFilters import EventFilters
import requests
import json
import time

# The callback function must only accept one parameter, which will be the event message data
def registerAudioLocation(data): #callback function 1
    print(data["message"])
    Msg = data["message"]
    element  = list(Msg.items())[0] # change 0 to the correct number to get the degree of arrival of speech
    print(element)

def registerAudioLocation_MetaData(data): # callback function 2
    print("Printing Meta data for audio localization......")
    print(data["message"])

if __name__ == "__main__":
    ipAddress = "IP ADRESS"
    misty = Robot(ipAddress)

    # Start recording audio
    file_to_record = {"FileName": "deleteThis.wav"}
    file = json.dumps(file_to_record, separators=(',', ':')) 
    url = "http://" + ipAddress + "/api/audio/record/start"
    r3_A = requests.post(url, json=file)
    print(r3_A.status_code)
    
    # Register for events to get the direction of sound and other meta data
    try:
        misty.RegisterEvent("soudnIn", Events.SourceTrackDataMessage,callback_function=registerAudioLocation, debounce = 100, keep_alive= True)
        #misty.RegisterEvent("soudnIn_meta", Events.SourceFocusConfigMessage,callback_function=registerAudioLocation_MetaData, keep_alive= True)

        #misty.KeepAlive()
    except Exception as ex:
        print(ex)
    finally:
        misty.UnregisterAllEvents() # Unregister events if they aren't all unregistered due to an error

    # wait for T seconds
    T = 1
    time.sleep(T)  

    #Stop Recording audio
    url = "http://" + ipAddress + "/api/audio/record/stop"
    r3_B = requests.post(url) 
    print(r3_B.status_code)
