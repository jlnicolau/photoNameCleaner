import sys
import os
import re
from pathlib import Path

#check if the folder already have a log. If yes, it will close the program to avoid to lose the previous log file.
if os.path.isfile("logFileNameChanges.txt"):
   sys.exit("The program will not execute because there is a logFile in the folder.")

#check if the path is valid
print(sys.argv[1])
pathRoot = Path(sys.argv[1])



for path in pathRoot.iterdir():
    print(path)
   


# if not os.path.isdir(photoRoot):
#     sys.exit("The given path doesn't exist.")

