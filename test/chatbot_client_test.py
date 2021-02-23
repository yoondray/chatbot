import socket
import json

host = "127.0.0.1"
port = 5050

while True:
    print("Question: ")
    query = input()
    if query == "exit":
        exit(0)
    print("=" * 40)

    mySocket = socket.socket()
    mySocket.connect((host, port))

    json_data = {
        'Query' : query,
        'BotType': "MyService"
    }

    message = json.dumps(json_data)
    mySocket.send(message.encode())

    data = mySocket.recv(2048).decode()
    ret_data = json.loads(data)

    print("Answer :")
    print(ret_data['Answer'])
    print("\n")

mySocket.close()