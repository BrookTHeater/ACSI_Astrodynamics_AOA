
import sys
from os import path

apistartup = "api_startup_file.txt"
#GmatInstall = r"C:\Users\grant\Downloads\gmat-win-R2022a\GMAT\api" <"EXAMPLE"
GmatBinPath = r"<!!Insert Path to GMAT Bin Folder!!>"
Startup = r"<Insert Path to Bin>\gmat-win-R2022a\GMAT\bin\api_startup_file.txt"


if path.exists(Startup):


   sys.path.insert(1, GmatBinPath)

   import gmatpy as gmat
   gmat.Setup(Startup)

else:
   print("Cannot find ", Startup)
   print()
   print("Please set up a GMAT startup file named ", apistartup, " in the ", 
      GmatBinPath, " folder.")
