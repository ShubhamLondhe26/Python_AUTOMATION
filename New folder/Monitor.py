#Automation process which displays all running process and 
# display memory consumption of each process.


import psutil

def Processdisplay():
    listprocess = []
    
    for proc in psutil.process_iter():
        try: 
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            
            pinfo['vms'] = proc.memory_info().vms/(1024*1024) #vms = virtual memory size
            
            listprocess.append(pinfo)
            
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
        
    return listprocess
    
def main():
    print('Automation process which displays all running process.')
    print('Process Monitor')
        
    listprocess = Processdisplay()
        
    for elem in  listprocess:
        print(elem)

if __name__=="__main__":
    main()