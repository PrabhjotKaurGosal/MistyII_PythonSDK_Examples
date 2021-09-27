import sys, os
import json
import requests
import base64
import pyimgur
from twilio.rest import Client

sys.path.append(os.path.join(os.path.dirname(__file__), '..')) 

# *************************************
# takephoto()
# Connects to Misty via https requests and takes picture with Rest API endpoint.
# Returns the Base64 string of the photo.
#
# *************************************
def takephoto():
    ip = "IP ADDRESS"
    url = "http://" + ip + "/api/cameras/rgb?base64=True&FileName=MyPicture&Width=800&Height=600&DisplayOnScreen=False"
    stringdata = requests.get(url, headers={'Content-Type': 'application/json'})
    a = stringdata.json()
    print(a)
    first_value = list(a.values())[0]
    fvalue2 = list(first_value.values())[0]
    print(fvalue2)
    return fvalue2

# *************************************
# mistytopc()
# Takes the base64 string from takephoto() and saves the image to pc.
#
# *************************************
def mistytopc(data): # can simplify 
    img = base64.b64decode(data)
    filename = 'mistyPhoto.jpg'
    with open(filename, 'wb') as f:
        f.write(img)

# *************************************
# uploadimg()
# Uploads image from PC to imgur with pyimgur.
# Needs account registered with imgur API following the instructions at https://apidocs.imgur.com/ 
# Returns the image link.
#
# *************************************
def uploadimg(PATH):
    CLIENT_ID = "CLIENT ID" 

    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")
    return uploaded_image.link

# *************************************
# sendmessage()
# 
# Sends the caption + image from imgur to user's phone number
# Needs an account registered with the Twilio API at twilio.com
#
# *************************************
def sendmessage(caption, contenturl):
    account_sid = "TWILIO ACCOUNT ID"
    auth_token = "TWILIO AUTH TOKEN"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to = "REGISTERED NUMBER",
        from_ = "TWILIO NUMBER",
        body = caption,
        media_url = contenturl)

    print(message.sid)

x = takephoto()
mistytopc(x)
y = uploadimg("./mistyPhoto.jpg ")
sendmessage("Photo", y)



# **************************************************************
# OTHER MISTY FUNCTIONS THAT WORKED WITH REST API ENDPOINTS

# WORKED
#ip = "IP ADDRESS"
#url = "http://" + ip + "/api/led"
#data1 = {"red": 108, "blue": 51, "green": 152}
#x = requests.post(url, data=json.dumps(data1), headers={'Content-Type': 'application/json'})
#print(x.text)

# MOVE ARM WORKED
#ip = "IP ADDRESS"
#url = "http://" + ip + "/api/arms"
#data1 = {"Arm": "Left", "Position": 0, "Velocity": 50}
#x = requests.post(url, data=json.dumps(data1), headers={'Content-Type': 'application/json'})
#print(x)

# MOVE HEAD WORKED
#ip = "IP ADDRESS"
#url = "http://" + ip + "/api/head"
#moveheadd = {"Pitch": -26, "Roll": -40, "Yaw": 40, "Velocity": 60}
#x = requests.post(url, data=json.dumps(moveheadd), headers={'Content-Type': 'application/json'})
#print(x)
