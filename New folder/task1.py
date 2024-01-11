import schedule
import time
import datetime

# def fun():
#     #add logic
#     print("Inside Fun")
    
# def main():
#     print("Inside Task Scheduler")
#     #calls EVERY on the default schedular instance
#     schedule.every(1).seconds.do(fun)
    
#     while(True):#unconditional infinite loop
#         schedule.run_pending()#runs all jobs that are scheduled to run.
#         time.sleep(1)#seconds #delay in execution of the program. 

# def fun():
#     #add logic
#     print("Inside Fun")
    
# def main():
#     print("Inside Task Scheduler")
#     #calls EVERY on the default schedular instance
#     schedule.every(1).minutes.do(fun)
    
#     while(True):#unconditional infinite loop
#         schedule.run_pending()#runs all jobs that are scheduled to run.
#         time.sleep(1)#seconds #delay in execution of the program. 

def fun():
    #add logic
    print("Inside Fun at the Time",datetime.datetime.now())
    
def main():
    print("Inside Task Scheduler")
    print("Current time:",datetime.datetime.now())
    schedule.every(10).seconds.do(fun)
    
    while(True):#unconditional infinite loop
        schedule.run_pending()#runs all jobs that are scheduled to run.
        time.sleep(1)#seconds #delay in execution of the program. 
        
if __name__=="__main__":
    main()