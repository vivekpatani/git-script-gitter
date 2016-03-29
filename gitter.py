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

def git_pusher(end_date = datetime.now(),start_date = datetime(2015,3,26,19,53,41)):

    delta = end_date - start_date
    print(delta.days)
    n = int(delta.days) + 1
    
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
    git_pusher(end_date = datetime(2016,3,29,19,53,41),start_date = datetime(2015,3,26,19,53,41))

if __name__ == "__main__":
    main()
    
