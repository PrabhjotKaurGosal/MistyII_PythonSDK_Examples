# This file simply tries to capture the image using various cameras on Misty

from mistyPy.Robot import Robot
from mistyPy.Events import Events
from mistyPy.EventFilters import EventFilters
import json
import requests
import base64
import numpy as np
import matplotlib.pyplot as plt

if __name__ =="__main__":
    try:
    # First create the robot object
        ip_address = "IP ADDRESS"
        misty = Robot(ip_address)

        ###### TakePicture using the RGB camera ---  GET Method <robot-ip-address>/api/cameras/rgb ... Base64 is a required parameter, rest are optional
        ###### Note: TakePicture takes a picture with Misty’s RGB camera.
        url = "http://" + ip_address + "/api/cameras/rgb?FileName=MistyRGB_img&Base64=True&Width=320&Height=240"
        r5 = requests.get(url, headers={'Content-Type': 'application/json'})  #returns a string containing the Base64-encoded image data, type and format of the image (jpeg), height and width
        print("The status of the TakePicture request is: ", r5.status_code)
                
        # Convert base64 string to .jpg format
        base64string_data = r5.json()
        encoded_image  = list(base64string_data.values())[0]
        encoded_image_value = list(encoded_image.values())[0]
        decoded_img = base64.b64decode(encoded_image_value)
        filename = 'mistyRGB.jpg'
        with open(filename, 'wb') as f:
            f.write(decoded_img)  #saves the decoded RGB image as mistyRGB.jpg

        ###### TakeDepthPicture ------  Get Method <robot-ip-address>/api/cameras/depth  .... Takes no parameters
        ###### Note: TakeDepthPicture takes a picture using  Misty’s Occipital Structure Core depth sensor
        url = "http://" + ip_address + "/api/cameras/depth"
        r6 = requests.get(url, headers={'Content-Type': 'application/json'}) # retuns  an object containing depth information about the image (array) that includes height, image array and width
        print("The status of TakeDepthPicture request is: ", r6.status_code)
        # image (array) - A matrix of size height x width containing individual values of type float. Each value is the distance in millimeters from the sensor for each pixel in the captured image.
        
        depth_image = list(r6.json().values())[0]
        depth_image_height =  list(depth_image.values())[0]
        depth_image_width =  list(depth_image.values())[2]
        depth_image_imagePythonList =  list(depth_image.values())[1]
        depth_image_imagePythonArray =  np.array(depth_image_imagePythonList) #convert list to array
        depth_image_imagePythonMatrix = np.reshape(depth_image_imagePythonArray, (depth_image_width,depth_image_height )) # reshape array
        print("The width of the depth image matrix is: ", depth_image_width)
        print("The height of the depth image matrix is: ",depth_image_height)
        print("The size of the depth image list is: ", len(depth_image_imagePythonList))
        #print(depth_image_imagePythonArray.shape)
        print("The size of the depth image matrix is: ", depth_image_imagePythonMatrix.shape)

        #plt.imshow(depth_image_imagePythonMatrix.astype(float))
        #plt.colorbar()
        #plt.show()

        ###### TakeFisheyePicture ------  Get Method <robot-ip-address>/api/cameras/fisheye .... Takes no parametersBase64 is a required parameter
        ###### Note: TakeFisheyePicture takes a picture using Misty’s Occipital Structure Core depth sensor
        url = "http://" + ip_address + "/api/cameras/fisheye?Base64=True"
        r7 = requests.get(url, headers={'Content-Type': 'application/json'}) #returns a base64 string
        print("The status of TakeFisheyePicture request is: ", r7.status_code) 

         # Convert base64 string to .jpg format
        base64string_data = r7.json()
        encoded_image  = list(base64string_data.values())[0]
        encoded_image_value = list(encoded_image.values())[0]
        decoded_img = base64.b64decode(encoded_image_value)
        filename_fishEye = 'mistyFishEye.png'
        with open(filename_fishEye, 'wb') as f:
            f.write(decoded_img)

        print("The width of the fisheye image is: ", list(encoded_image.values())[5])
        print("The height of the fisheye image is: ", list(encoded_image.values())[2])
        
    except Exception as ex:
        print(ex)
    finally:
    # Unregister events if they aren't all unregistered due to an error
        misty.UnregisterAllEvents()



        ####### EXpected Results #########
        # The status of the TakePicture request is:  200
        # The status of TakeDepthPicture request is:  200
        # The width of the depth image matrix is:  320
        # The height of the depth image matrix is:  240
        # The size of the depth image list is:  76800
        # The size of the depth image matrix is:  (320, 240)
        # The status of TakeFisheyePicture request is:  200
        # The width of the fisheye image is:  640.0
        # The height of the fisheye image is:  480.0

        # Additionally, it will create and save two image files (one for the output from the RGB camera and one for the output from the Fisheye camera)