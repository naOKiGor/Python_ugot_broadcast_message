uGot_Broadcast_message Python library

```
from ugot_broadcast_message import ugot_broadcast_channel
channel = ugot_broadcast_channel()

# Optional set communication channel, default is 0
# channel.set_channel(0)

# Enable broadcast function, default is off
channel.set_enable(True)

# Set message received callback #1: use lambda
channel.set_message_received_callback(lambda message_content: print(message_content))

# Set message received callback #2: use regular function
def message_received_handler(message_content: str):
	print(message_content)

channel.set_message_received_callback(message_received_handler)

# Set message received callback #3: use annotation
@channel.set_message_received_callback
def message_received_handler(message_content: str):
	print(message_content)

# Send broadcast message to current channel
channel.send_broadcast_message('Hello world')

# Send unicast message to specify address
channel.send_message_to('Hello world', address='10.11.12.13')
```
