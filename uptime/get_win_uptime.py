'''
Python Script to Log System Uptime 
'''

# OS and Logging for logging function
import os
import logging

# Arguments - Requried for CLI Agruments
import argparse

# Required to get hostname
import socket

# ctypes required for using GetTickCount64()
import ctypes


# Arguments - Initialize parser
parser = argparse.ArgumentParser()
 
# Arguments - Adding optional argument
parser.add_argument("-q", "--quiet", action="store_true", help="log only, run without output to screen")
parser.add_argument("-L", "--logfile", help="specify logfile")

# Arguments - Read arguments from command line
args = parser.parse_args()


# Setup Logging Environment
scriptBasename = (os.path.splitext(os.path.basename(__file__))[0])
myhostname = socket.gethostname()
logfile = scriptBasename + '-' + myhostname + '.log'

logging.basicConfig(filename=logfile, encoding='utf-8', level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)-7s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

 
# getting the library in which GetTickCount64() resides
lib = ctypes.windll.kernel32
 
# calling the function and storing the return value
t = lib.GetTickCount64()
 
# since the time is in milliseconds i.e. 1000 * seconds
# therefore truncating the value
t = int(str(t)[:-3])
 
# extracting hours, minutes, seconds & days from t
# variable (which stores total time in seconds)
mins, sec = divmod(t, 60)
hour, mins = divmod(mins, 60)
days, hour = divmod(hour, 24)
 
# formatting the time in readable form
# (format = x days, HH:MM:SS)

if args.quiet:
    print("Displaying Output as: % s" % args.quiet)
    logging.info(f"{myhostname} - System Uptime: {days} days, {hour:02}:{mins:02}:{sec:02}")
elif args.logfile:
    # DO NOTHING FOR NOW
    ("Displaying Output as: % s" % args.logfile)
else: # Dfault print to screen
    print("\n")
    print(f"  System Uptime: {days} days, {hour:02}:{mins:02}:{sec:02}")
    print("\n")
    input("  Press Enter to continue...")








 
 

 
