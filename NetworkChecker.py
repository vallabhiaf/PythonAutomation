#Requests is a Python module that you can use to send all kinds of HTTP requests. It's an easy-to-use library with a lot of features ranging from passing parameters in URLs to sending custom headers and SSL verification. You can add headers, form data, multi-part files, and parameters with simple Python dictionaries.You can then access the response data using the same request.

#sudo apt install python3-requests                                                                                                          File: network.py

#!/usr/bin/env python3
import requests
import socket
def check_localhost():
        localhost = socket.gethostbyname('localhost')
        if localhost == "127.0.0.1":
                return true
def check_connectivity():
        request = requests.get("http://www.google.com")
        if request == 200:
                return true
































