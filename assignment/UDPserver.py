# UDP Receiver server
# ET1524 Assignment 2

from socket import *

# Port number
serverPort = 12000

# Create UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind socket to port
serverSocket.bind(("", serverPort))

print("Receiver is ready...")

# Expected sequence number
expectedSequence = 10001

while True:

    # Receive packet
    message, clientAddress = serverSocket.recvfrom(2048)

    # Convert bytes to string
    message = message.decode()

    # Split message at ";"
    parts = message.split(";")

    # Extract sequence number
    sequenceNumber = int(parts[0])

    # Print received packet number
    print("Received packet:", sequenceNumber)

    # Detect packet loss
    if sequenceNumber > expectedSequence:

        print("Packet loss detected!")
        print("Expected:", expectedSequence)
        print("Received:", sequenceNumber)

    # Detect out-of-order packets
    elif sequenceNumber < expectedSequence:

        print("Out-of-order packet detected!")

    # Update expected sequence number
    expectedSequence = sequenceNumber + 1