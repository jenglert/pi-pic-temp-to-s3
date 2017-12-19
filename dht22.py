
"""  
Temperature/Humidity monitor using Raspberry Pi and DHT22. 
Data is displayed at thingspeak.com
Original author: Mahesh Venkitachalam at electronut.in 
Modified by Adam Garbo on December 1, 2016 
""" 
import sys 
import RPi.GPIO as GPIO 
from time import sleep 
import Adafruit_DHT 
import urllib2 
def getSensorData(): 
	RH, T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 23) 
	temp = '{0:0.1f}'.format((T * 1.8 + 32))
	return ('{0:0.1f}'.format(RH), temp) 
def main(): 
	print 'starting...' 
 	while True: 
		try: 
			RH, T = getSensorData() 
			print "Humidity:" + RH + " Temperature:" + T
			sleep(3)  
	    	except: 
			print 'exiting.' 
			break 

# call main 
if __name__ == '__main__':
	main()  
