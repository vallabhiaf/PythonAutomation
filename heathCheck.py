#beforerunning give exectue permission with
#chmod +x healthCheck.py
#run with
#./healthCheck.py

#shebang
#!/usr/bin/env python3

#checkDiskUsage
import shutil
du=shuti.disk_usage("/")
percentage=du.free/du.total*100

#cpu_percent
import psutil
psutil.cpu_percent(0.1)
