import socket
import soundcard as sc 
from os import _exit
import pickle
default_speaker = sc.default_speaker()
def playaudio(data):
    
    with default_speaker.player(samplerate=48000) as sp:
        sp.play(data)
with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:

    print('created socket')

    port = 8001

    try:
        host_ip = '127.0.0.1'
    except socket.gaierror:
        print('shouldn\'t see this ever')

    s.bind((host_ip,port))

    
    print('socket is listening')
    socketdata = []
    while True:
        # conn,addr=s.accept()
        data=s.recv(4096)
        print("DATA {}".format(data) )
        if not data: break
        socketdata.append(data)
    comp = pickle.loads(b"".join(socketdata))
    print(comp)
    # playaudio(comp)
    
    # while True:
        
    #     cmd = input('CMD: ')
    #     if cmd[:4] == 'exit':
    #         _exit(0)
    
                
                

            
        