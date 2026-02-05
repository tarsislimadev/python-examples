# docker run -d --name rabbitmq -p 5672:5672 rabbitmq

# pip install pika

import pika

rabbitmq_host = "localhost"

# Connect to RabbitMQ server (default: localhost)
connection = pika.BlockingConnection(pika.ConnectionParameters(rabbitmq_host))
channel = connection.channel()

# Declare a queue (idempotent: creates if not exists)
queue_name="hello"
channel.queue_declare(queue=queue_name)

# Publish a message
channel.basic_publish(exchange="", routing_key="hello", body="Hello RabbitMQ!")

print("Sent 'Hello RabbitMQ!'")

# Close connection
connection.close()
