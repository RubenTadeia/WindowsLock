import os, sys

def setConfigVars(key, pathToScript):
	configFile = str(pathToScript) + '\\vars.config'
	with open(configFile) as fi:
		lines = fi.readlines()
		for line in lines:
			line = line.replace('\n','')
			content = line.split(",,")
			if content[0] == key:
				return content [1]
		return

def writeInFile(FilePath,text):
	with open(FilePath,'w') as f:
		f.write(text)
		f.close()