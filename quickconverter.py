#Version 1.0.0
#This program was written by Anonemous2 4/27/2019
#It simply converts .fbx(s) and .png(s)into .papa(s)

#import os subprocess module
import os

#main function
def main():
    #create a list of files
    foundFiles = []
    foundFilesCheck = []
    #check directory
    directory = os.path.dirname(os.path.realpath(__file__))
    directory = directory.replace('\\','/')
    print(directory)
    #create a loop that will discover all files within the tools directory, then add them to the list
    print("---START---")
    print("The following files have been found:")
    for root, dirs, files in os.walk(directory):
        for fileName in files:
            #print the file found
            print(fileName)
            #add file to list
            foundFiles.append(fileName)
    #check list for required files
    #find default.settings
    if 'default.settings' in foundFiles:
        foundFiles.remove('default.settings')
    else:
        #print error
        print("ERROR: default.settings is missing from this directory")
    #find papatran.exe
    if 'papatran.exe' in foundFiles:
        foundFiles.remove('papatran.exe')
    else:
        #print error
        print("ERROR: papatran.exe is missing from this directory")
    #find and remove quickconverter and papadump from the list
    if 'papadump.exe' in foundFiles:
        foundFiles.remove('papadump.exe')
    if 'quickconverter.py' in foundFiles:
        foundFiles.remove('quickconverter.py')
    print("---CONVERTING---")
    #begin coverting files
    command = f'cd {directory}'
    os.system(command)
    #fist find the amount of files
    count = len(foundFiles)
    #look at each file, and determine if it can be converted.
    for file in foundFiles:
        #determine if it is a .fbx
        if file.find('.fbx') != -1:
            #strip off .fbx
            fileShort = file.replace('.fbx', '')
            command = f'papatran.exe --texture-mode reference -o {fileShort}.papa {fileShort}.fbx'
            os.system(command)
            #check for success
            for root, dirs, files in os.walk(directory):
                for fileNameCheck in files:
                    #add all files to a new list, this will include any new files
                    foundFilesCheck.append(fileNameCheck)
            fileToCheck = f'{fileShort}.papa'
            if fileToCheck in foundFilesCheck:
                #print success
                print(file, ' was successfully converted into a .papa', sep="")
            else:
                #print error
                print('ERROR: ', file, ' was not converted.', sep="")
        #determine if it is a .png
        elif file.find('.png') != -1:
            #strip off .png
            fileShort = file.replace('.png', '')
            command = f'papatran.exe --texture-mode include -o {fileShort}.papa {fileShort}.png'
            os.system(command)
            #check for success
            for root, dirs, files in os.walk(directory):
                for fileNameCheck in files:
                    #add all files to a new list, this will include any new files
                    foundFilesCheck.append(fileNameCheck)
            fileToCheck = f'{fileShort}.papa'
            if fileToCheck in foundFilesCheck:
                #print success
                print(file, ' was successfully converted into a .papa', sep="")
            else:
                #print error
                print('ERROR: ', file, ' was not converted.', sep="")
        #determine if it is a .papa
        elif file.find('.papa') != -1:
            print(file, ' is already a .papa', sep="")
        #else print error
        else:
            print('ERROR: ', file, ' cannot be converted into a .papa', sep="")
        count -= 1
        if count == 0:
            break
            
main()
    
#end of program
print("---END---")
