from mistyPy.Robot import Robot
from mistyPy.Events import Events
import matplotlib.pyplot as plt 
import numpy as np
import base64
import requests
import json

ipAddress = 'Misty IP Address'

# CONVERT DEPTH PHOTO TO MATRIX
def toMatrix(l, n):
    matrix = []
    for i in range (0, len(l), n):
        matrix.append(l[i:i+n])
    return matrix

# TAKE DEPTH PHOTO AND CONVERT TO MATRIX 
def depthsave(ip):
    #send request for misty to take depth photo
    url = "http://" + ip + "/api/cameras/depth?Base64=true"  
    r1 = requests.get(url, headers={'Content-Type': 'application/json'})
    returnr = r1.json()
    y = (returnr['result']['image'])

    notNan = 0

    # set NaN values equal to 0 
    for i in range(len(y)):
        if y[i] == 'NaN':
            y[i] = 0
        else:
            # find how many values in the array were not NaN (they were successful
            notNan += 1
    print(notNan)

    # convert array to matrix, save grayscale image to folder
    imageMatrix = toMatrix(y, returnr['result']['width'])

    plt.imshow(imageMatrix)
    plt.gray()
    # plt.show() if want to show image directly
    plt.savefig('DEPTH PHOTO NAME.png', bbox_inches='tight')

# SAVE FISHEYE BASE64 STRING TO IMAGE TO COMPUTER
def fisheye(ip):
    url = "http://" + ip + "/api/cameras/fisheye?Base64=true"
    r1 = requests.get(url, headers={'Content-Type': 'application/json'})
    returnr = r1.json()
    x= returnr['result']['base64']

    img = base64.b64decode(x)
    filename = 'FISHEYE IMAGE NAME.png'
    with open(filename, 'wb') as f:
        f.write(img)

depthsave(ipAddress)
fisheye(ipAddress)