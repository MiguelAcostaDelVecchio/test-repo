from dronekit import connect, VehicleMode, LocationGlobalRelative, APIException
import time
import socket 
import math
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

def arm():
	#vehicle.is_armable=True
	#while vehicle.is_armable==False:
	#	print('Waiting for vehicle to become armable')
	#	time.sleep(1)
	print("vehicle is armable")
	print("")
   	
	vehicle.armed=True
	while vehicle.armed==False:
		print("waiting for drone to become armed")
		time.sleep(1)
	print("vehicle is now armed")
	print("Motors are spinning!!! Its working!!!")

	return None

vehicle = connectMyCopter()
arm()
print("end of script")

