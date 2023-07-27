import socket

while(True):

    print("[1]" + " Find port")
    print("[2]" + " Find service")
    print("[3]" + " Exit")
    print(" ")
    num = int(input("Enter an option: "))

    if num == 1:
        protocol = input("Enter the service protocol: ")
        port = socket.getservbyname(protocol)
        print("The port: " + str(port))
        print(" ")

    if num == 2:
        ports = int(input("Enter the port: "))
        service = socket.getservbyport(ports)
        print("The service: " + service)
        print(" ")
    if num == 3:
        exit(0)

