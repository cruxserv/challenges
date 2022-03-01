# Operating system name and version
import os
import platform
import socket
import ipify

print("Operating system:", platform.system(), "Version:", platform.release())
# Primary private IP
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print("Private IP: ", local_ip)
# Primary public IP

ip = ipify.get_ip()
# EC2 instance type
# EC2 instance ID
# import os
# command = "dig TXT +short o-o.myaddr.l.google.com @ns1.google.com | awk -F\'\"\' '{print $2}' "
# ip = os.system(command)
