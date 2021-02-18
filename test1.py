import paho.mqtt.client as mqtt #import the client1
import time
import random

broker_address="io.adafruit.com"
clientId="Dwi" #ganti sesuai nama kalian
username= "DwiAS" #Ganti sesuai username kalian
password= "aio_vPZX572tBKoEW9BIBAGimou0XV5a" #ganti sesuai token API kalian
topic1 = "sensor-suhu-dalam-ruang" # ganti sesuai key sensor yang mau kalian masukin
topic2 = "sensor-suhu-luar-ruang"
topic3 = "sensor-suhu-ac"

#broker_address="iot.eclipse.org" #use external broker
client = mqtt.Client("hai") #create new instance
client.username_pw_set(username, password)
client.connect(broker_address) #connect to broker
i = 23
j = 25
k = 18
while True:
    #publish
    client.publish(username+"/feeds/"+topic1,i)
    client.publish(username + "/feeds/" + topic2, j)
    client.publish(username + "/feeds/" + topic3, k)
    if (i > 25):
        i= i + random.randint(-2,0)
    else:
        i = i + random.randint(0,2)
    j = i + random.randint(0,3)
    time.sleep(15)