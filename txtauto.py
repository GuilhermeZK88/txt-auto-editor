filePath = 'test.txt'

try:
    with open(filePath, 'r') as file:
        print(file.readline())
#except (FileNotFoundError, IOError) as errormsg:
#        print(errormsg, 'penus')