# This file provides an example of registering to Misty's Events to get live data using an Event Object (as opposed to using the callback function)

from mistyPy.Robot import Robot
from mistyPy.Events import Events
from mistyPy.EventFilters import EventFilters
 
if __name__ == "__main__":
    try:
        ### First create the robot object
        ip_address = "IP ADDRESS"
        misty = Robot(ip_address)

        ### EXAMPLE 1: Register to the IMU event
        EventData = misty.RegisterEvent("IMU_data", Events.IMU)

        # Wait for the event to get some data before printing the message
        while "just waiting for data" in str(EventData.data):
            pass
        Msg = EventData.data["message"]
        print("Printing the message from the IMU Event ..... ")
        print(Msg)
        IMU_yaw = Msg['yaw']
        print("The IMU yaw is: ", IMU_yaw)

        ### EXAMPLE 2: Register to the ActuatorPosition Event with added filters
        DataHeadYaw = misty.RegisterEvent("Actuator_headYaw", Events.ActuatorPosition, condition=[EventFilters.ActuatorPosition.HeadYaw])

        # Wait for the event to get some data before printing the message
        while "just waiting for data" in str(DataHeadYaw.data):
            pass
        MsgHeadYaw = DataHeadYaw.data["message"]
        print("Printing the message from the ActuatorPosition event .... ")
        print(MsgHeadYaw)
        Head_Yaw = MsgHeadYaw['value']
        print("The Head yaw is: ", Head_Yaw)

        ### Use the KeepAlive function to keep running the main python thread until all events are closed, or the script is killed due to an exception
        # misty.KeepAlive()

    except Exception as ex:
        print(ex)
    finally:
        # Unregister events if they aren't all unregistered due to an error
        misty.UnregisterAllEvents()

########## Expected Output ###################
# Printing the message from the IMU Event ..... 
# {'created': '2021-07-17T16:14:06.1595679Z', 'pitch': 359.6456080036178, 'pitchVelocity': 0.05729577951308232, 'roll': 0.17188733853924698, 'rollVelocity': 0.0, 'sensorId': 'imu', 'xAcceleration': 0.03, 'yAcceleration': 0.05, 'yaw': 11.3445643435903, 'yawVelocity': 0.0, 'zAcceleration': -9.8}
# The IMU yaw is:  11.3445643435903
# Printing the message from the ActuatorPosition event .... 
# {'actuatorId': '2ABzJD', 'created': '2021-07-17T16:14:07.3538065Z', 'rawValue': None, 'sensorId': 'ahy', 'value': 0.0}
# The Head yaw is:  0.0