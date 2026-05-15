# ET1524 – Assignment 2

## Streaming via UDP and TCP

---

# Connection to Assignment 1

In Assignment 1, I learned the basics of network communication using Python sockets.

I created:

* a UDP client and server
* a TCP client and server
* a simple HTTP web browser using sockets

The programs used IP addresses and ports to send and receive messages between a client and a server.

Example from Assignment 1:

Client:

```python
message = input("Input lowercase sentence:")
clientSocket.sendto(message.encode(), (serverName, serverPort))
```

Server:

```python
message, clientAddress = serverSocket.recvfrom(2048)
print(message.decode())
```

In Assignment 1, only one message was sent at a time.

Example transmitted data:

```text
hello
```

or:

```text
GET / HTTP/1.1
```

---

# Transition to Assignment 2

Assignment 2 is based on the same UDP and TCP socket communication from Assignment 1.

Instead of sending only one message manually, the program now sends many packets continuously to simulate streaming traffic such as:

* video streaming
* audio streaming
* online games

The original UDP client code was modified by:

* adding loops
* adding sequence numbers
* adding payload data
* using the sleep() function to control packet speed

---

# Example Streaming Packet

Example packet structure:

```text
10001;AAAAAAAAAAAA#### 
```

Explanation:

* 10001; → sequence number
* AAAAAAAA → payload data
* #### → end marker

The sequence number is used to detect:

* packet loss
* out-of-order packets

---

# Important Concepts

## Socket

A socket is used for communication over the network.

## UDP

UDP is fast and connectionless, but packets can be lost or arrive in the wrong order.

## TCP

TCP creates a connection and guarantees reliable and ordered delivery.

## Packet

A packet is a small piece of data sent through the network.

## sleep()

The sleep() function controls how fast packets are sent.

Example:

* 20 packets/sec → sleep(0.05)
* 45 packets/sec → sleep(0.022)

Without sleep(), packets would be sent too quickly.
