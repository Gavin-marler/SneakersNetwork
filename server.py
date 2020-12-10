import socketserver
import socket
import pandas  

sneaker_data = pandas.read_csv("StockX-Data-Contest-2019-3.csv", low_memory=False)

class Sneaker_Stat_Server(socketserver.BaseRequestHandler):

    def handle(self):
        source_ip_address = self.client_address[0]
        source_port = self.client_address[1]

        source_msg = str(self.request[0], "UTF-8") 
        print("[{}:{}] => {}".format(source_ip_address, source_port, source_msg))

        try:
            result = str(sneaker_data[source_msg].min())
        except:
            result = str(-1)

        sock = self.request[1]
        sock.sendto(bytes(result, "UTF-8"), self.client_address)

        print("[{}:{}] <= {}".format(source_ip_address, source_port, result))
        

host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)
server_address = (ip_address, 5000)
print("Starting Server: [{}:{}]".format(server_address[0], server_address[1]))

with socketserver.UDPServer(server_address, Sneaker_Stat_Server) as server:
    server.serve_forever()