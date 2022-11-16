import re

# The filePath variable must be assigned to the file path of the file
# you want this program to edit using double '\'. For example:
# filePath = 'C:\\Documents\\ThisFile.txt'
filePath = 'test.txt' # CHANGE ME!
newDate = '1969-08-18' # CHANGE ME!

backupPath = 'backupAutoTxt.txt' # You may change me!


dateRegEx = '[0-9?][0-9?][0-9?][0-9?]-[0-9?].?-[0-9?].?'

try:
    with open(filePath, 'r+') as ogFile, open(backupPath, 'w') as buFile:
        # Reading original file, and copying content to backup
        oldContent = ogFile.read()
        buFile.write(oldContent)

        # Substituting dates to variable newDate content
        newContent = re.sub(dateRegEx, newDate, oldContent)
        ogFile.seek(0)
        ogFile.write(newContent)
        ogFile.truncate()   

        # Printing original content and substituted content
        print(oldContent)
        print(newContent)

except (FileNotFoundError, IOError) as errormsg:
        print(errormsg)

# Program ran
print('txtauto.py finished running.')