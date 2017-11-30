import os
import socket
import time

from zeroconf import ServiceBrowser, ServiceStateChange, Zeroconf

import subprocess

machines = []

def scan_machine(ip,port_start,port_end):
    for port in range(port_start,port_end):
        # print(port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.01)
        result = sock.connect_ex((ip,port))
        if result == 0:
            print str(port) + " is open"
        else:
            pass


def on_service_state_change(zeroconf, service_type, name, state_change):
    if state_change is ServiceStateChange.Added:
        info = zeroconf.get_service_info(service_type, name)
        if info:
            machines.append(str(socket.inet_ntoa(info.address)))
            # print("IP:" + str(socket.inet_ntoa(info.address)))

zeroconf = Zeroconf()

print("Scanning Raspberry Pi...")
browser = ServiceBrowser(zeroconf, "_workstation._tcp.local.", 
handlers=[on_service_state_change])

time.sleep(2)
zeroconf.close()

if os.name == 'nt':
    print("Scanning computers...")
    proc = subprocess.Popen("net view", stdout=subprocess.PIPE)
    netview_result = proc.stdout.read().split()
    for result in netview_result:
        if result[0] == '\\':
            machines.append(result[2:])
            # print(result[2:])

# print(machines)
for machine in machines:
    print("Scanning : " + machine)
    scan_machine(machine,42001,43999)