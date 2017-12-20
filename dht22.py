
import sys 
import RPi.GPIO as GPIO 
from time import sleep 
import Adafruit_DHT 

def getSensorData(): 
	RH, T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 23) 
	temp = '{0:0.1f}'.format((T * 1.8 + 32))
	return ('{0:0.1f}'.format(RH), temp) 
def main(): 
	RH, T = getSensorData() 
        print RH + "-" + T

# call main 
if __name__ == '__main__':
	main()  
