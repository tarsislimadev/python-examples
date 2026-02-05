# docker run -d --name rabbitmq -p 5672:5672 rabbitmq

# pip install pika

import pika

rabbitmq_host = "localhost"

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters(rabbitmq_host))
channel = connection.channel()

# Ensure the queue exists
queue_name='hello'
channel.queue_declare(queue=queue_name)

# Define callback function to process messages
def callback(ch, method, properties, body):
  print(f"Received {body.decode()}")

# Subscribe to the queue
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
