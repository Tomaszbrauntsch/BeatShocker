import psutil
import pywintypes
import win32api
def getpid():
    for proc in psutil.process_iter():
        if proc.name() == "UnityPlayer.dll":
            return proc.pid

my_pid = getpid()
PROCESS_ALL_ACCESS = 0x1F0FFF
processHandle = win32api.OpenProcess(PROCESS_ALL_ACCESS, False, my_pid)
modules = win32process.EnumProcessModules(processHandle)
processHandle.close()
base_addr = modules[0] # for me it worked to select the first item in list...
