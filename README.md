# Gitter Python  

## Prerequisites  
1.) Python 3.5.1+ or it should be working with Python 2.7+ with a few mods.  
2.) Git installation  
3.) SSH Setup for Git (Refer: https://help.github.com/articles/generating-an-ssh-key/)  

## How to Run:  
Ignore Step 1 if you have setup the git repo and configured your ssh for that repo.  
1.) Run the following commands first: (If you cannot follow: https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/)  
Copy the gitter.py in this folder first.  
Run command Prompt and type the following:  
```{r}
git init  
git add .
git commit -m
git remote add origin git@github.com:username/reponame.git  
[The above should be SSH URL and not HTTPS, you can find this link on https://github.com/username/repo-name]  
git push origin master
``` 

2.) After you've done the first step once, you need to run the script  
If Windows,  
```{r}
go to the folder with the script  
Press Shft + RightMouseButton  
Open Command Prompt here  
Type in the command prompt  
$ python gitter.py
```  
  
3.) Now to change the dates:
```{r}
open gitter.py
In the main() function the call to git_pusher() is called.  
git_pusher() accepts two parameters
end_date = "The date which would the higher bound where the last git commit will be made" (Using Python Date Format)  
start_date = "The date onwards which you want to push a commit everyday until the end_date" (Using Python Date Format)  
```
![The Main Function](/input.png)

## Output  
![The Git Hub Push Output](/git.png)
![The Git Hub Color](/output.png)

## My 2 cents to the community.