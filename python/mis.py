from mpu6050 import mpu6050
import time
import math
from datetime import datetime

sensor = mpu6050(0x68)

fn=datetime.now().strftime("%Y-%m-%d_%H:%M:%S")+".csv"

while True:
	a_data=sensor.get_accel_data()

	pitch = (math.atan2(a_data["y"], a_data["z"])+math.pi)*57.295779513082320876798154814105
	#print(int(pitch))
	roll = (math.atan2(a_data["x"], a_data["z"])+math.pi)*57.295779513082320876798154814105
	#print(roll)
	yaw = (math.atan2(a_data["x"], a_data["y"])+math.pi)*57.295779513082320876798154814105
	#print(yaw)
	print("Pitch: "+str(int(pitch))+" Roll: "+str(int(roll))+" Yaw: "+str(int(yaw)))

	#g_data = sensor.get_all_data()
	g_data = sensor.get_all_data()
	#print(g_data[0])

	f = open(fn,'a')
	f.write(str(datetime.now())+","+str(int(pitch))+","+str(int(roll))+","+str(int(yaw))+","+str(g_data[0]['x'])+","+str(g_data[0]['y'])+","+str(g_data[0]['z'])+","+str(g_data[1]['x'])+","+str(g_data[1]['y'])+","+str(g_data[1]['z'])+"\n") #csv output
	## Python will convert \n to os.linesep
	#f.close()

	time.sleep(0.05)


#pitch = (math.atan2(accel_t_gyro.value.y_accel, accel_t_gyro.value.z_accel)+math.pi)*57.295779513082320876798154814105
#double roll = (math.atan2(accel_t_gyro.value.x_accel, accel_t_gyro.value.z_accel)+PI)*57.295779513082320876798154814105;
#double yaw = (math.atan2(accel_t_gyro.value.x_accel, accel_t_gyro.value.y_accel)+PI)*57.295779513082320876798154814105;