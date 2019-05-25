import socket

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:

    print('created socket')

    port = 8001

    try:
        host_ip = '127.0.0.1'
    except socket.gaierror:
        print('shouldn\'t see this ever')

    s.bind((host_ip,port))

    s.listen(10)
    print('socket is listening')

    while True:
        conn,addr=s.accept()
        data=conn.recv(1024)
        print(data)