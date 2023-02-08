
import serial

if __name__ == '__main__':
	ser=serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
	ser.flush()
	
	while True:
		if  ser.in_waiting > 0:
 			data=ser.readline().decode('utf-8').rstrip()
			print(type(data)+ " "+data)
			if data == "1":
				print("got")


'''def espeak():
	espeak.synth('Hello')
	espeak.synth('Welcome to SJEC')'''


