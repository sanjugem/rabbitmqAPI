#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('admin', 'pass')
parameters = pika.ConnectionParameters('sanju-gem.noip.me',5672,'shost',credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.exchange_declare(exchange='node2',type='topic')

result = channel.queue_declare('light1',exclusive=False)
queue_name = result.method.queue

channel.queue_bind(exchange='node2',routing_key='light',queue=queue_name)

print ' [*] Waiting for logs. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] %r" % (body,)

channel.basic_consume(callback,queue=queue_name,no_ack=True)

channel.start_consuming()