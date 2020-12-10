import socket

print("Welcome to the Sneaker Network. This simple program was designed to show the concept of networking.")
ip_address = input("Enter Sneaker Server IP Address: ")
request = input("Enter 'Sale Price' to Find the price of the cheapest shoe sold on StockX in 2019")

server_address = (ip_address, 5000)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.sendto(bytes(request, "UTF-8"), server_address)
    result = str(sock.recv(1024), "UTF-8")
    print("Result: "+result)