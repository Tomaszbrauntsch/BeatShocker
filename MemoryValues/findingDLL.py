import pefile

exe_path = "D:/Games/SteamLibrary/steamapps/common/Beat Saber/Beat Saber.exe"
pe = pefile.PE(exe_path)

for entry in pe.DIRECTORY_ENTRY_IMPORT:
    dll_name = entry.dll.decode('utf-8')
    if dll_name == "UnityPlayer.dll":
        for func in entry.imports:
            unityPlayer_hexaddress = ("%08x" % func.address)

# firstPointer = "0154D848"
# secondPointer = "6E0"
# thirdPointer = "20"
# fourthPointer = "1C8"
# fifthPointer
print (unityPlayer_hexaddress)
