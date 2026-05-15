# UDP Sender client
# ET1524 Assignment 2


from socket import * 
from time import sleep  # Import sleep function to create delay between packets

# Receiver IP address
# 127.0.0.1 means same computer (localhost)
serverName = "127.0.0.1"

# Port number
serverPort = 12000

# Create UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)  # AF_INET = IPv4, SOCK_DGRAM = UDP

# Number of packets to send
numberOfPackets = 20 

# Packets per second
packetsPerSecond = 1 

# Time delay between packets
# Example:
# 1 packet/sec = 1 second delay
# 20 packets/sec = 0.05 seconds delay 
# 45 packets/sec = 0.022 seconds delay
sleepTime = 1 / packetsPerSecond    #sleep() controls packet sending speed ..

# Start sequence number
sequenceNumber = 10001  

# Send packets in a loop
for i in range(numberOfPackets):

    # Create sequence number
    # Example: 10001;
    message = str(sequenceNumber) + ";"

    # Fill packet with data
    # 1465 bytes payload
    message += "A" * 1465 # Fill packet with payload data

    # End marker
    message += "####"

    # Send packet to receiver
    clientSocket.sendto(message.encode(), (serverName, serverPort))

    # Print sent packet number
    print("Sent packet:", sequenceNumber)

    # Increase sequence number
    sequenceNumber += 1

    # Wait before next packet
    sleep(sleepTime)

# Close socket
clientSocket.close()