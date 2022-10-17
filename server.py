import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
print('Python server is running..')

temperature = "100F"
precipitation = "20%"
dailyLow = "70"
dailyHigh = "110"


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT)) #The .bind() method is used to associate the socket with a specific network interface and port number
    s.listen() #enables a server to accept connections
    conn, addr = s.accept() #The .accept() method blocks execution and waits for an incoming connection.
    #When a client connects, it returns a new socket object representing the connection and a tuple holding the address of the client. 
    #The tuple will contain (host, port) for IPv4 connections 
    
    with conn:
        print(f"Connected by client: {addr}")
        conn.send(bytes("The average temperature today will be 100F.There is a 20% chance of precipitation.  The high temperature today will be 110F.  The low will be 70F.","utf-8"))


