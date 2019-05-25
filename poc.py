import soundcard as sc 

speakers = sc.all_speakers()
print(speakers)
speaker=sc.default_speaker()
inputsp=sc.default_loopback_device()