import os
import subprocess
cmd='cd "E:\\user\\Google Drive\\MADNERD\\github\leds\\arduino\" && platformio run'
# result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
try:
    result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
except:
    result = "Failed"
print("---------------------------------")
print result
print ("--------------------------------")
