from djitellopy import tello
from time import sleep

drone = tello.Tello()
drone.connect()
print(drone.get_battery())


drone.takeoff() # Drone takes off
drone.send_rc_control(0, 50, 0, 0) # Go forward 50cm
sleep(2) # Halt code for 2 seconds
drone.send_rc_control(0, 0, 0, 0)  # Reseting the forward direction so drone stays still
drone.land() # Landing drone
