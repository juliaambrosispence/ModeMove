#ModMove 1.0
#By j. beans
#CC BY-SA 4.0

import os, sys, io, shutil, time

print("\nModMove 1.0 by j. beans\n")

modsPath = ""

while not os.path.exists(modsPath):
	print("Please enter your Steam directory.\n(No input will default to C:\Program Files (x86)\Steam)")
	modsPath = input()
	if modsPath == "":
		modsPath = "C:\Program Files (x86)\Steam\steamapps\workshop\content\\211820"
	else:
		modsPath += "\steamapps\workshop\content\\211820"
	if not os.path.exists(modsPath):
		print(modsPath, "is an invalid directory!\n")
	
destPath = ""
while not os.path.exists(destPath):
	print("Now enter your Starbound installation folder.\n(No input will default to C:\Program Files (x86)\Steam\steamapps\common\Starbound)")
	destPath = input()
	if destPath == "":
		destPath = "C:\Program Files (x86)\Steam\steamapps\common\Starbound\mods"
	else:
		destPath += "\mods"
	if not os.path.exists(destPath):
		print(destPath, "is an invalid directory!\n")
	


strDvd = "--------------------------------------------------------------------------------------------------------------"

startTime = time.time()

print(strDvd)
print("Moving mods from", modsPath)
print("To", destPath)
print(strDvd)
print()

#IGNORE FIRST LOOP
first = True
loopCount = 0
movedCount = 0
for root, dirs, files in os.walk(modsPath, True):
	if not first:
		loopCount += 1
		movedCount += 1
		#print(strDvd)
		normroot = os.path.normpath(root)
		normrootlist = normroot.split(os.sep)
		finalNamePath = destPath + "\\" + normrootlist[-1] + ".pak"
		
		if not len(files) == 0:
			filePth = root + "\\" + files[0]
			print("Copying", filePth)
		
			shutil.copy(filePth, destPath)
			interFilePath = destPath + "\\" + "contents.pak"
			print("To", interFilePath)

			print("Renaming to", finalNamePath)
			try:
				os.rename(interFilePath, finalNamePath)
			except OSError:
				print("This file already exists!")
				print("Skipping...")
				os.remove(interFilePath)
				movedCount -= 1
		else:
			print("No file in", root)
			movedCount -= 1
		
		print(strDvd)
		print()
		
	else:
		first = False

currentTime = time.time()
elapsed = currentTime - startTime

print("File copy completed in", round(elapsed, 3), "seconds.")
print("Attempted", loopCount, "directories.")
print("Copied", movedCount, "files.")
input("\nClose...")