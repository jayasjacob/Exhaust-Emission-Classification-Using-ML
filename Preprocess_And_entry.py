#Author Jayas P Jacob

import serial
import time
import csv

Vin=5
Ro=2
Vin=(float)(Vin)
Ro=(float)(Ro)



ser = serial.Serial('COM4')
ser.flushInput()

while True:
    
    try:
        ser_bytes = ser.readline()
        decoded_bytes = float(ser_bytes[0:len(ser_bytes) - 2].decode("utf-8"))
        print(decoded_bytes)
        Vres=Vin*(decoded_bytes/Ro)
        Rs=Vres/decoded_bytes
        Vres=(float)(Vres)
        Rs=(float)(Rs)
        with open("mcA4.csv", "a", newline='') as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerow([decoded_bytes/abs(decoded_bytes),decoded_bytes/1024,
              decoded_bytes/1022,
              decoded_bytes,
              decoded_bytes*abs(decoded_bytes-1024),
              decoded_bytes*abs(decoded_bytes-1022),
              decoded_bytes*abs(Rs/Ro),
              decoded_bytes-Ro/1024,
              decoded_bytes-Ro/1022,
              decoded_bytes-Rs*abs(Ro),
              decoded_bytes*(Vin-Vres),
              decoded_bytes*(Vin/Vres)*1024,
              decoded_bytes*(Vin/Vres)*1022,
              decoded_bytes/Vres,
              decoded_bytes/Vin*abs(Vres-Rs),
              Vres/decoded_bytes-(1024*Ro/Vin)])
    except:
        print("Keyboard Interrupt")
        break