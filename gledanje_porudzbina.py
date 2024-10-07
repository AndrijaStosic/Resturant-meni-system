import socket

def send_order(order):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))  
    client_socket.send(order.encode())  
    client_socket.close()


narudzbina = "Porudzbina: Pica, Kola"  
send_order(narudzbina)
