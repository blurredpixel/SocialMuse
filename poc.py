import soundcard as sc 
import socket

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    print('created socket')

    default_speaker = sc.default_speaker()
    mics = sc.all_microphones(include_loopback=True)
    print(mics[0])

    loopback = sc.get_microphone('Audio',include_loopback=True)
    s.connect(('127.0.0.1',8001))
    with loopback.recorder(samplerate=48000) as mic, default_speaker.player(samplerate=48000) as sp:
        while True:
            data=loopback.record(numframes=1024,samplerate=48000)
            
            s.sendall(data.copy(order='C'))
            sp.play(data)