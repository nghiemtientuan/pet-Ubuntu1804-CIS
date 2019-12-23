import subprocess, re, os

def replaceLine(filePath, pattern, replaceString):
	found = False
	with open(filePath, 'a+') as file:
		lineList = file.readlines()

	for key, line in enumerate(lineList):
		if (re.search(pattern, line)):
			found = True

			if (re.search("^[^#]" + replaceString, line)):
				return False
			else:
				lineList[key] = replaceString + '\n'

				f = open(filePath, "w+")
				f.writelines( lineList )
				f.close()

				return True

    # if string not found, ad new line in end file
	if (found == False):
		with open(filePath, 'a+') as file:
			file.write('\n' + replaceString)

	return True

def checkMountOptionSet(optionSet):
	mount = subprocess.Popen('mount', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	for line in mount.stdout.readlines():
		if (not re.search(optionSet, line)):
			return False

	return True

def mountOptionSet(optionSet):
	mount = subprocess.Popen('mount', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	for line in mount.stdout.readlines():
		source, afterOn = line.split(' on ')
		command = "sudo mount -o remount," + optionSet + " "
		command += source
		os.popen(command)

	return True

def removeStringInLine(filePath, delString):
	with open(filePath, 'a+') as file:
		lineList = file.readlines()

	for key, line in enumerate(lineList):
		if (delString in line):
			before, after = line.split(' ' + delString)
			lineList[key] = before + after

			f = open(filePath, "w+")
			f.writelines( lineList )
			f.close()

	return True

def checkDisableServiceInFile(filePath, serviceName):
	with open(filePath, 'a+') as file:
		lineList = file.readlines()

	for key, line in enumerate(lineList):
		if (re.search('disable[\s]+=[\s+]', line) and not re.search('disable[\s]+=[\s+]yes', line)):
			return False

	return True


def checkDisableServiceInFolder(folderPath, serviceName):
	if (not os.path.exists(folderPath)):
		os.mkdir(folderPath);
	for file in os.listdir(folderPath):
		if (serviceName in file):
			filePath = folderPath + '/' + file

			check = checkDisableServiceInFile(filePath, serviceName)
			if (check == False): return False

	return True

def disableServiceInFolder(folderPath, serviceName):
	for file in os.listdir(folderPath):
		if (serviceName in file):
			filePath = folderPath + '/' + file

			with open(filePath, 'a+') as file:
				lineList = file.readlines()

			for key, line in enumerate(lineList):
				if (re.search('disable[\s]+=[\s+]', line) and not re.search('disable[\s]+=[\s+]yes', line)):
					before, after = line.split(' ' + delString)
					lineList[key] = before + '= yes' 

					f = open(filePath, "w+")
					f.writelines( lineList )
					f.close()