import requests
import os
import ctypes

krnl = ctypes.WinDLL("kernel32")
user = ctypes.WinDLL("user32")
console = krnl.GetConsoleWindow()
user.ShowWindow(console,0)

#link: https://github.com/Luckytrang2010/rickroll/blob/main/rickroll.mp4?raw=true
rick_roll = requests.get("https://github.com/Luckytrang2010/rickroll/blob/main/rickroll.mp4?raw=true")

output = rick_roll.content
rr = open("./lol.mp4","wb")
rr.write(output)
rr.close()

os.system("{}\\lol.mp4".format(os.getcwd()))
