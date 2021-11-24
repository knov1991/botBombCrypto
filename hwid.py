import sys
import time
import subprocess

def hwid():
    try:
        if sys.platform.startswith("windows"):
            #MacAdressCheck
            mac = subprocess.Popen("getmac", shell=True,stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
            return mac
        else:
            #HwidCheck
            hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
            return hwid
    except:
                print('ERRO')