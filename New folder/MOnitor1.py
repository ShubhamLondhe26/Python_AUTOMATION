import psutil

#return a sorted list of current running process

print(psutil.pids())

#psutil.process_iter(attrs=None,ad_value+None)
# return an iterator yeilding a process class instance fo all running processs
#on the local machine

for proc in psutil.process_iter(['pid','name']):
    print(proc.memory_info())