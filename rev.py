import argparse
import re
import os.path
import os
import shutil
import time
import sys


ALLOWED_FILES = ['srt']

def ParseInput():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="the input file or directory")
    args = parser.parse_args()

    f = args.input
    print(f)
    if f:
        if (os.path.isfile(f)):
            return [f]
        elif (os.path.isdir(f)):
            fileList = GetFileList(f)
            return fileList
        elif (os.path.isdir(f[:-1])):
            fileList = GetFileList(f[:-1])
            return fileList
    return None

def GetFileList(dir):
    list = []
    for f in os.listdir(dir):
        #print(f)
        if os.path.isfile(os.path.join(dir, f)):
            if (re.split('[.]', f)[-1] in ALLOWED_FILES):
                list.append(os.path.join(dir, f))
    return list
		
def ReversePuctuation(file, newfile):
    f = open(file, 'r', encoding="Windows-1255")
    nf = open(newfile, 'w', encoding="Windows-1255")
    
    #print("both files opened")
    for line in f:
        if len(line)>2:
            nf.write(FixOneLine(line[:-1]) + line[-1])
        else:
            nf.write(line)
    f.close()
    nf.close()
	
def FixOneLine(s):
    SpecialChars = '.,:;''()-?!+=*&$^%#@~`" /'
    Prefix = ''
    Suffix = ''
    
    while (len(s) > 0 and s[0] in SpecialChars):
        Prefix += s[0]
        s = s[1:]
    
    while (len(s) > 0 and s[-1] in SpecialChars):
        Suffix += s[-1]
        s = s[:-1]
        
    if Prefix == ' -':
        Prefix = '- '
    if Suffix == ' -':
        Suffix = '- '
    
    return Suffix + s + Prefix

def Main():
    fileList = [" ".join(sys.argv[1:])]
    if (not fileList):
        print('Usage: Select file')
        return
        
    #print (fileList)
    print("Found " + str(len(fileList)) + " files. Starting to convert")
    
    for file in fileList:
        print("Converting File: " + re.split(r'[\\]', file)[-1])
        
        # define file names
        if re.split('[.]', file)[-2] == 'REV':
            newFile = ".".join(re.split('[.]', file)[:-2]) + ".srt"
        else:
            newFile = ".".join(re.split('[.]', file)[:-1]) + ".REV.srt"
        
        
        ReversePuctuation(file, newFile)
        
        #os.remove(file)

    print ('total files: ' + str(len(fileList)))
    
    time.sleep(1)


if __name__ == '__main__':
    Main()
