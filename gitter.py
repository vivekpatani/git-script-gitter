import os
import subprocess
from datetime import datetime
from datetime import date
from datetime import timedelta
import random
#from dateutil.relativedelta import relativedelta

def calling(git_date):
    changes = ["Added new Updates","Code cleanup","Removed Failing Function","Ready for release","Hotfix A101","Feature update 00321"]
    element = random.choice(changes)
    subprocess.call("git --version")
    subprocess.call("git status")
    subprocess.call("git add .")
    os.environ["GIT_COMMITTER_DATE"] = str(git_date)
    subprocess.call("git commit -am \""+str(element) +"\" --date="+str(git_date))
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

def git_single_push_today(git_date=datetime.now()):

    print(git_date)
    calling(git_date)
    with open("./logwa.txt","a") as log:
        pushed = "Pushed for " + str(git_date) + "\n"
        log.write(str(git_date))
    print(git_date)
    git_date = ""

    log.close()

def main():
    #git_single_push_today()
    git_pusher(end_date = datetime(2016,5,16,19,53,41),start_date = datetime(2016,4,27,19,53,41))

if __name__ == "__main__":
    main()
