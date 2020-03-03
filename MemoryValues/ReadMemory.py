# import ctypes
# from ctypes import *
# from ctypes.wintypes import *
# import psutil
# import sys
#
# mainProcess = "firefox.exe"
# missAddress = 0x003E001C
# readSize = 256
#
# def getpid():
#     for proc in psutil.process_iter():
#         if proc.name() == "firefox.exe":
#             return proc.pid
#
# PROCESS_VM_READ = 0x0010
#
# if getpid() == None:
#     print ("Number: ", mainProcess)
#     sys.exit()
# else:
#     PID = getpid()
#     print(PID)
#
# #Everything above works
# # TODO: Making the finding of a value and extracting that value possible of address
#
# process = windll.kernel32.OpenProcess(PROCESS_VM_READ,0,PID)
# readprocmem = windll.kernel32.ReadProcessMemory
# readBuffer = ctypes.create_string_buffer(readSize)
# print("Done processing")
# for i in range(1,100000):
#     try:
#         if readprocmem(process,hex(i),readBuffer,readSize,0):
#             print(readBuffer.raw)
#     except:
#         None
# print("Finished")

#Requirement of kernel32: https://docs.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-openprocess
#Process Permissions: https://docs.microsoft.com/en-us/windows/win32/procthread/process-security-and-access-rights
#Don't use process_all_access it will require the program to have much more on then what it really needs
#
#hProcess = Process we are going to work with
#lpBaseAddress is the memory address you will be working with
#

import ctypes
import psutil

#DLLS needed
kernel32 = ctypes.windll.kernel32
#Process Permissions
PROCESS_QUERY_INFORMATION = (0x0400)
PROCESS_VM_OPERATION = (0x0008)
PROCESS_VM_READ = (0x0010)
#Windows API's
OpenProcess = kernel32.OpenProcess
CloseHandle = kernel32.CloseHandle
GetLastError = kernel32.GetLastError
ReadProcessMemory = kernel32.ReadProcessMemory

class ReadMemory:
    def OpenProcess(self, hProcess):
        dwDesiredAccess = (PROCESS_QUERY_INFORMATION | PROCESS_VM_OPERATION | PROCESS_VM_READ)
        bInheritHandle = False
        #This loop checks for the proces pid that matches the process we want
        for Process in psutil.process_iter():
            if Process.name() == hProcess:
                dwProcessId = Process.pid
                hProcess = OpenProcess(dwDesiredAccess, bInheritHandle, dwProcessId)
                return hProcess
            elif Process.name == None:
                hProcess = None

    def CloseHandle(self, hProcess):
        CloseHandle(hObject)

    def GetLastError(self):
        GetLastError()
        return GetLastError()

    def PointerOffset(self, memoryAddress):
        pass

    def ReadProcessMemory(self, hProcess, memoryAddress):
        try:
            BaseAddress  = memoryAddress
            readBuffer = ctypes.c_uint()
            bABuffer = ctypes.byref(readBuffer)
            bAnSize = ctypes.sizeof(readBuffer)
            bANumberOfBytesRead = ctypes.c_ulong(0)

            ReadProcessMemory(hProcess, memoryAddress, bABuffer, bAnSize, bANumberOfBytesRead)
            return readBuffer.value
        except(BufferError, ValueError, TypeError):
            CloseHandle(hProcess)
            e = 'Handle Close, Error', hProcess, GetLastError()
            return e

readMem = ReadMemory()
