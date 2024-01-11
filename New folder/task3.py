#Q.3 Design automation script which accept directory  name from user and create log file in that directory which contains information of running processes and its name,PID, Username

import psutil
import os
import sys

def mkdirec(dname):
    try:
        os.mkdir(dname)
        print("Directory created")
    except FileExistsError:
        print("Directory already exists.")
def create_file(name):
    
        
# def Processdisplay():
#     listprocess = []
    
#     for proc in psutil.process_iter():
#         try: 
#             pinfo = proc.as_dict(attrs=['pid','name','username'])
            
#             pinfo['vms'] = proc.memory_info().vms/(1024*1024) #vms = virtual memory size
            
#             listprocess.append(pinfo)
            
#         except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
#             pass
        
#     return listprocess

    
def main():
    drec1 = input("Enter the directory name:")
    mkdirec(drec1)
    filename = input("Enter the file name:")
    create_file(filename)
    
    # print('Automation process which displays all running process.')
    # print('Process Monitor')
        
    # listprocess = Processdisplay()
        
    # for elem in  listprocess:
    #     print(elem)
        
if __name__=="__main__":
    main()