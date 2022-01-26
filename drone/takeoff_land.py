from dronekit import connect, VehicleMode, LocationGlobalRelative 
import time 
import socket
#import exceptions
import argparse

def connectMyCopter():
	# Connecting to actual drone
	"""
	parser = argparse.ArgumentParser(description='commands')
	parser.add_argument('--connect')
	args = parser.parse_args()

	connection_string = args.connect
	baud_rate = 57600
	
	vehicle = connect(connection_string, baud=baud_rate, wait_ready=True)
	return vehicle
	"""

	# Connecting to Simulation
	parser = argparse.ArgumentParser(description='commands')
	parser.add_argument('--connect')
	args = parser.parse_args()
	
	connection_string = args.connect
	
	if not connection_string:
		import dronekit_sitl
		sitl = dronekit_sitl.start_default()
		connection_string = sitl.connection_string()

	vehicle = connect(connection_string, wait_ready=True)
	
	return vehicle


def arm_and_takeoff(aTargetAltitude):
	while not vehicle.is_armable:
		print("Waiting for vehicle to become armable")
		time.sleep(1)
	vehicle.mode = VehicleMode("GUIDED")
	while vehicle.mode!="GUIDED":
		print("Waiting for vehicle to enter GUIDED mode")
		time.sleep(1)

	vehicle.armed = True
	while vehicle.armed == False:
		print("Waiting for vehicle to become armed.")
		time.sleep(1)

	vehicle.simple_takeoff(atargetAltitude)

	while True:
		print("Current Altitude: %d"%vehicle.location.global_relative_frame.alt)
		if vehicle.location.global_relative_frame.alt>aTargetAltitude*.95:
			break
		time.sleep(1)

	print("Target altitude reached")
	return None

vehicle=connectMyCopter()
print("About to Takeoff")

vehicle.mode=VehicleMode("GUIDED")
arm_and_takeoff(20) # fly to altitude of 20 meters
vehicle.mode = VehicleMode("LAND") # Once target altitude is reached, drone will land

time.sleep(2)

print("End of function")
print("ArduCopter version: %s"%vehicle.version)

while True:
	time.sleep(2)

vehicle.close()
# End of script

