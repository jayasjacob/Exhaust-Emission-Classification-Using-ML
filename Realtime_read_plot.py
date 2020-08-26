#Author: Jayas P Jacob
#Digital Signature:7FG3DF4ERS5GG56749JYU7634ILKHJ37DF2EAQW2ZXC234DFG5HTY7UIRK
import serial
import matplotlib.pyplot as plt
#import seaborn as sns
import numpy as np
plt.ion()
plt.style.use('ggplot')
#sns.set()
fig=plt.figure()
fig, ax = plt.subplots()


i=0
x=list()
y=list()
i=0
ser = serial.Serial('COM4',9600)
ser.close()
ser.open()
while True:

    data1 = ser.readline()
    print(data1.decode())
    x.append(i)
    y.append(data1.decode())

    plt.scatter(i, float(data1.decode()))


    ax.bar(i, float(data1.decode()))



    i += 1
    plt.show()


    plt.pause(0.0001)


