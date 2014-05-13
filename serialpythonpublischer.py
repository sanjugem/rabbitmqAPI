import serial
import time
import pika
import sys


ser = serial.Serial(port='/dev/ttyAMA0',baudrate=115200,timeout=0.2)
#ser.write("100")
#ser.open()

try:
	credentials = pika.PlainCredentials('admin', 'pass')
	parameters = pika.ConnectionParameters('localhost',5672,'shost',credentials)
	connection = pika.BlockingConnection(parameters)
	channel= connection.channel()
	while 1:
		if (ser.inWaiting() > 0):
		    response = ser.readline(None)
		    ser.flushInput()  ##flush input after reading
		    #ser.flushOutput()
		    response=response.strip()
		    if response :    
			    
			    
			    #channel.exchange_declare(exchange='node2',type='topic',durable='true', arguments={"arg1":"test"})
			    channel.exchange_declare(exchange='node2',type='topic')
			    message= response
			    channel.basic_publish(exchange='node2',routing_key='light',body=message)
			    #channel.basic_publish(exchange='node1',routing_key='light',body=message)
			    #channel.queue_declare(queue='temperature',exclusive='true')
			    #channel.queue_declare(queue='light',exclusive='true')
			    #channel.queue_bind(exchange='node1',queue='temperature',routing_key='temperature')
			    #channel.queue_bind(exchange='node1',queue='light',routing_key='light')

			    print " [x] Sent %r" % (message,)
	connection.close()

			    #print time.ctime(time.time())
except KeyboardInterrupt:
	ser.close()
