import serial
import time

ser = serial.Serial('/COM3', 9600, timeout=1)
time.sleep(2)

ser.write(b'Josh is the man!')


message = ser.read(ser.in_waiting).decode('utf-8').rstrip()
print(message)

ser.close()