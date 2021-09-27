# This file provides an example of registering to one of the Misty's Events to get live data using a CALLBACK function

from mistyPy.Robot import Robot
from mistyPy.Events import Events
from mistyPy.EventFilters import EventFilters

# The callback function must only accept one parameter, which will be the event message data
# Within this callback function, the users can describe anything that they wish to do with the data from Misty's Events.
# In this example, we simply print the data on the screen
def callback_func(data):
    print(data)
    print("Printing message only ...")
    print(data["message"])
    print("Printing the first (key:value) pair in the message .......")
    Msg = data["message"]
    element  = list(Msg.items())[0]
    print(element)
   
if __name__ == "__main__":
    try:
        ### First create the robot object
        ip_address = "IP ADDRESS"
        misty = Robot(ip_address)

        ### Register the event, which has a minimum of 2 parameters: the user defined name of the event, and the event type 
        misty.RegisterEvent("battery_charge", Events.BatteryCharge,callback_function=callback_func, keep_alive= False) # Register to BatteryCharge event
        # misty.RegisterEvent("source_track_data_message", Events.SourceTrackDataMessage,callback_function=callback_func, keep_alive = False)

        ### Use the KeepAlive function to keep running the main python thread until all events are closed, or the script is killed due to an exception
        # misty.KeepAlive()

    except Exception as ex:
        print(ex)
    finally:
        # Unregister events if they aren't all unregistered due to an error
        misty.UnregisterAllEvents()

########## Expected Output ###################
# {'eventName': '7464431873', 'message': {'chargePercent': 0.83, 'created': '2021-07-08T07:09:01.6610701Z', 'current': -0.411, 'healthPercent': 0.63, 'isCharging': False, 'sensorId': 'charge', 'state': 'Discharging', 'temperature': 0, 'trained': True, 'voltage': 7.772}}
# Printing message only ...
# {'chargePercent': 0.83, 'created': '2021-07-08T07:09:01.6610701Z', 'current': -0.411, 'healthPercent': 0.63, 'isCharging': False, 'sensorId': 'charge', 'state': 'Discharging', 'temperature': 0, 'trained': True, 'voltage': 7.772}
# Printing the first (key:value) pair in the message .......
# ('chargePercent', 0.83)
# Event connection has closed for event: battery_charge