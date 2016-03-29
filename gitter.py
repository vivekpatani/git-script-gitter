import os
import subprocess
from datetime import datetime
from datetime import date
from datetime import timedelta
#from dateutil.relativedelta import relativedelta

def calling(git_date):
    subprocess.call("git --version")
    subprocess.call("git status")
    subprocess.call("git add .")
    os.environ["GIT_COMMITTER_DATE"] = str(git_date)
    subprocess.call("git commit -am \"Changing Things\" --date="+str(git_date))
    subprocess.call("git push origin master")
    
    #temp = input("Enter to close:")

def date_calc():
    today = date(2014,4,21)
    yesterday = today - timedelta(days=1)
    print(today,yesterday)

def git_pusher(n=1,end_date = datetime.now(),start_date = datetime(2014,1,1,19,53,41)):

    print(end_date.isoformat())
    delta = start_date - end_date
    print(delta.days)

    if int(delta.days) > n:
        n = delta

    print(delta)
    while True:
        break
    for i in range(0,n):
        current = start_date + timedelta(days=i)
        print(current)
        calling(current.isoformat())
        pushed = "Pushed for " + str(current) + "\n"
        with open("./logwa.txt","a") as log:
            log.write(pushed)
        current = ""
        
    log.close()

def main():
    git_pusher(n=50,end_date = datetime(2016,3,29,15,48,12),start_date = datetime(2016,2,12,19,53,41))
    #calling()
    #date_calc()

if __name__ == "__main__":
    main()
    
