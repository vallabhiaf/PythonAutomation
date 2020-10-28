#path is neccessary
import os
os.remove("novel.txt")
os.rename("old_name.txt","new_name.txt")
#check_weather the file exists

os.path.exists("Vallabh.txt")
os.path.getsize("Vallabh.txt")
#findthe time when the file was last modified.the return is a timestamp since 1970(unix file systems time convention)
timestamp=os.path.getmtime("Vallabh.txt")
datetime.datetime.fromtimestamp(timestamp)#converting to date
#to find the aboslute path
os.path.abspath("Vallabh.txt")
os.cwd()#currentdirectorty
os.mkdir("new_directory")
os.chrdir("new_directory")
os.listdir("web")#list the files

for name in os.listdir(dir):
  fullname=os.path.join(dir,name)
  if os.path.isdir(fullname):
    print("{} is a directory".foramat(fullname))
  else:
    print("{} is a file".format(fullame))
