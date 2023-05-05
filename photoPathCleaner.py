# -*- coding: utf-8 -*-

# this program was made for 'POSIX' systems only. (Linux)
# this program is able to verify and change characters in files name and paths. 
# HOW TO USE
# at the prompt :/photoPathCleaner.py <path> <characteres_to_change> <character_to_use> <OPTION>
# characteres_to_change: any set of letters or regex.
# character_to_use: one string only. Usually, one letter or symbol.
# Options:  --justlog it creates a log file containing the paths and the fix that would be done.
#           --rename it creates a log file containing the paths and the fix that was done.


import sys
import os
import re

#check if the folder already have a log. If yes, it will close the program to avoid to lose the previous log file.
if os.path.isfile("logFileNameChanges.txt"):
   sys.exit("The program will not execute because there is a logFile in the folder.")

#check if the path is valid
photoRoot = sys.argv[1]
if not os.path.isdir(photoRoot):
    sys.exit("The given path doesn't exist.")

#check if the argument is valid.
mode = sys.argv[4]
if mode == "--justlog":
   logFile = open("logFileNameChanges.txt", "a")
   logFile.write("JUST LOG MODE, the files were not changed.\n")
elif mode == "--rename":
   logFile = open("logFileNameChanges.txt", "a")
   logFile.write("RENAME MODE, the files were not changed.\n")
else:
   sys.exit("The argument wasn't recognized.")

# the repr returns raw string with quotes. The [1:-1] removes the quotes
charToFind = repr(sys.argv[2])[1:-1] 

# the repr returns raw string with quotes. The [1:-1] removes the quotes
charToUse = repr(sys.argv[3])[1:-1]
logFile.write("Changing '" + charToFind + "' to '" + charToUse + "." + "'\n")

#it checks the file system. If "nt", windows. If "posix", Linux/Unix/MacOS
#if os.name == 'nt':
#   separator = '\\'
#   print(repr(separator))
#   logFile.write("Operational System: Windows"+"\n\n")
#else:
#   separator = '/'
#  logFile.write("Operational System: MacOs/Linux/Unix"+"\n\n")

  
#Walk through the folder checking for strange characteres
for root, dirs, files in os.walk(photoRoot):
   for dir in dirs:
      hasBadCharactere=re.search(charToFind, dir)
      #when it finds a strange caractere, it builds the bad path string. From the bad path, it reconstructs the good path string (character by character) changing the bad ones.
      if hasBadCharactere:
         print(root)
         print(dir)
         wrongPathName = root+"/"+dir
         rightPathName = ""
         for c in wrongPathName:
            if re.search(charToFind, c):
               rightPathName = rightPathName + charToUse
            else:
               rightPathName = rightPathName + c
         
         # it only renames in --rename mode.      
         if mode == "--rename":
            print(wrongPathName)
            print(repr(wrongPathName))

            os.rename(wrongPathName, rightPathName)

         logFile.write("[DIR ] " + wrongPathName + "\n=====> " + rightPathName + "\n\n"  )
         print("[DIR ] " + wrongPathName + "\n======> " + rightPathName +"\n\n")
         

for root, dirs, files in os.walk(photoRoot):
   for file in files:
         hasBadCharactere=re.search(charToFind, file)
         if hasBadCharactere:
            print(root)
            print(file)
            wrongFileName = file
            rightFileName = ""
            for c in wrongFileName:
               if re.search(charToFind, c):
                  rightFileName = rightFileName + charToUse
               else:
                  rightFileName = rightFileName + c

            # rename the file if the program is in rename mode
            if mode == "--rename":
               os.rename(repr(root+"/"+wrongFileName, root+"/"+rightFileName))

            logFile.write("[FILE] " + root+"/"+wrongFileName + "\n=====> " + root+"/"+rightFileName + "\n\n" )
            print("[FILE ] " + wrongFileName + "\n======> " + rightFileName +"\n\n")
logFile.close()      
print('End of the program')

