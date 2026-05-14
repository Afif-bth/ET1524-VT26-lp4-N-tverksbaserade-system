from socket import *

serverName = "www.ingonline.nu"
serverPort = 80

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))

request = "GET /tictactoe/index.php?board=xoxoeoeex HTTP/1.1\r\n"
request += "Host: www.ingonline.nu\r\n"
request += "Connection: close\r\n\r\n"

clientSocket.send(request.encode())

response = ""

while True:
    data = clientSocket.recv(1024)
    if not data:
        break
    response += data.decode(errors="ignore")

print(response)

clientSocket.close()