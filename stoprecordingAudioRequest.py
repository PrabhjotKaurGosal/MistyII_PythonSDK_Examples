from mistyPy.Robot import Robot
from mistyPy.Events import Events
from mistyPy.EventFilters import EventFilters
import json
import requests
import time

if __name__ =="__main__":
        # First create the robot object
        ip_address = "IP ADDRESS"
        misty = Robot(ip_address)
 

    #  Stop Recording audio
        url = "http://" + ip_address + "/api/audio/record/stop"
        r3_B = requests.post(url) # Note, POST request for Misty expects a JSON payload
        print(r3_B.status_code)
