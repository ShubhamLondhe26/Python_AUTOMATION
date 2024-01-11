#Q.4 schedule task by hour , minut day in 3 diff function 


import schedule
import datetime
import time


def hour():
    print("Task for this Hour:",datetime.datetime.now())
def minutes():
    print("Task for this Minute:",datetime.datetime.now())
def day():
    print("Task for this Day:",datetime.datetime.now())
    
def main():
    print("Inside Task Scheduler")

    schedule.every(1).hour.do(hour)
    schedule.every(1).minutes.do(minutes)
    schedule.every().monday.at("13:00").do(day)
    
    while(True):
        schedule.run_pending()
        time.sleep(1)
    
if __name__=="__main__":
    main()