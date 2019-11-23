import re

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
				lineList[key] = replaceString

				f = open(filePath, "w+")
				f.writelines( lineList )
				f.close()

				return True

    # if string not found, ad new line in end file
	if (found == False):
		with open(filePath, 'a+') as file:
			file.write('\n' + replaceString)

	return True