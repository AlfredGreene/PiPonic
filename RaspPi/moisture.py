#!/usr/bin/python

import MySQLdb
import serial
import re
import time

conn = MySQLdb.connect(host="localhost", user="root", passwd="tortuga", db="data")
ser = serial.Serial('/dev/ttyACM0', 9600)

cursor = conn.cursor()

#!=====! To create a new database !======!
#Will change to arg variables
#cursor.execute("DROP TABLE IF EXISTS data")
#sql = "CREATE TABLE data (date TIMESTAMP NOT NULL,elapsed INT(10) NOT NULL, moisture INT(10) NOT NULL, temperature INT(10) NOT NULL, light INT(10) NOT NULL)"
#cursor.execute(sql)

#Wait for arduino to boot
time.sleep(3)

moisture, temp, light = 1,1,1

addData = "INSERT INTO data (elapsed, moisture, temperature, light) VALUES (%d, %d, %d, %d)"

#Flush the serial buffer
ser.readline()

elapsedTime = 0

print "===================="
try:
	while(1):
		time.sleep(1)
		readings = ser.readline()
		elapsedTime = elapsedTime + 1
		readings = re.sub('\r\n', '', readings)
		print "Sensor Readings"
		print readings
		data = str(readings).split("\t")
		if(len(data)==3):
			print "Data: ", data
			moisture, temp, light = data
			
			if(moisture.isdigit() and temp.isdigit() and light.isdigit()):
				
				celcius = (int(temp)) *(5000/1024)
				print "celcius1:", celcius
				celcius = (celcius/1024)
				print "celcius1:", celcius
				celcius = ((celcius-0.5) *100)
				print "celcius1:", celcius

				celcius = ((celcius - 500)/10)
				print "celcius1:", celcius
				
				print "===================="
				print "Moisture: ", moisture
				print "Temperature: ", temp
				print "Light: ", light
				print "===================="
		
		try:
			cursor.execute("INSERT INTO data (elapsed, moisture, temperature, light) VALUES (%s, %s, %s, %s)",(elapsedTime, moisture, temp, light))
			conn.commit()
		except:
			conn.rollback()

		print(cursor.execute("SELECT * FROM data"))

except KeyboardInterrupt:
		conn.close()
		print "/nDone Logging Data."
