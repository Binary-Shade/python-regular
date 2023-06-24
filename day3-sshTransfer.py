#!/usr/bin/env python3

import paramiko as pk
import getpass as gp

#ssh credentials
print("+------------------------------+")
print("|       SSH FILE TRANSFER      |")
print("+------------------------------+")

port=22
host_ip=input("Enter the host ip :")
user_name=input("Enter the user name :")
password=gp.getpass("Enter the password :")

#path 
remote_path=input("Enter the remote path of the file :")
local_path=input("Enter the local path to save :")

client=pk.SSHClient()
client.set_missing_host_key_policy(pk.AutoAddPolicy()) #to authenticate with ssh keys

try:
    client.connect(host_ip,port,user_name,password)
    print("client connected")
    sftp=client.open_sftp() #sftp client
    print("sftp client initialized")
    # sftp.put(local_path, remote_path)
    sftp.get(remote_path,local_path)
    print("file transfered")
    sftp.close()
    
except Exception as e:
    print("connection error! maybe connection refused by host"+str(e))
finally:
    client.close()
