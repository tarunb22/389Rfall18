#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket
import hashlib

host = "142.93.117.193"   # IP address or URL
port =  7331    # port

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# receive some data
data = s.recv(1024).decode()

data_list = data.split()
data_list = data_list[9:]

while(data_list[0] == "Find"):
    print(data_list[3])
    hex = ""
    if(data_list[3] == "sha512"):
        hex = str(hashlib.sha512(data_list[6].encode()).hexdigest())
    elif(data_list[3] == "sha1"):
        hex = str(hashlib.sha1(data_list[6].encode()).hexdigest())
    elif(data_list[3] == "sha384"):
        hex = str(hashlib.sha384(data_list[6].encode()).hexdigest())
    elif(data_list[3] == "sha256"):
        hex = str(hashlib.sha256(data_list[6].encode()).hexdigest())
    elif(data_list[3] == "md5"):
        hex = str(hashlib.md5(data_list[6].encode()).hexdigest())
    elif(data_list[3] == "sha224"):
        hex = str(hashlib.sha224(data_list[6].encode()).hexdigest())
    s.send((hex + "\n").encode())
    data = s.recv(1024).decode()
    data_list = data.split()
    print(data_list)
    data_list = data_list[1:]

# close the connection
s.close()
