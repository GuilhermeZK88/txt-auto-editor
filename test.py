import os #listdir, path.exists, makedirs
from csv import reader
from re import sub
from datetime import datetime

# directory path where csv (info on how to) and txt (files to alter) reside

# Assuming the .csv info file is in the directory of this program, witch is accessed by:
dir_path = os.getcwd()
print(f'Searching CSV file in: {dir_path}')

file_list = os.listdir(dir_path)
date = str(datetime.now())[:10]
no_csv = True
# searching for csv file, to extract VARIABLE : VALUE pairs information
# VARIABLE is the target for substitution, using its VALUE value
for file_name in file_list:
    if '.csv' in file_name:
        no_csv = False
        print(f'Using info from file: {file_name}')
        # concatenating diretory path with file name, for file path
        file_path = dir_path + '//' + file_name
        
        with open(file_path) as csv_file:
            # object that reads each line of the .csv as lists            
            reading_csv = reader(csv_file)
            # skiping first row (column names)
            next(reading_csv)
            # creating dictionary with VARIABLE : VALUE pairs
            substituitions = dict((row[0],row[1]) for row in reading_csv)

            for var, value in substituitions.items():
                print(f'{var:^30} -> {value}')

            # if no value given, assumes folder where this programa is
            if substituitions['folder_with_txt'] == '':
                # removing this .csv file from future iterations in this code run
                file_list.remove(file_name)
            # if a value is given, use it as path to find .txt files folder
            else:
                # updating dir_path and its files list
                dir_path = substituitions['folder_with_txt']
                file_list = os.listdir(dir_path)
        # stopping further .csv search
        break

# Checking for .csv instructions/variables file
if no_csv:
    raise ValueError('Found no .csv file!')

# If output folder still doesn't exists, creating it
try:
    new_folder_name = '\AutoTxtEditorResults_' + date + '\\'
    outfile_folder_path = dir_path + new_folder_name
    os.mkdir(outfile_folder_path)
    print(f'Created new folder: {new_folder_name}')
except FileExistsError:
    print(f'Updating folder {new_folder_name} content.')
    pass

print(f'Searching TXT files in: {dir_path}')

for file_name in file_list:
    if '.txt' in file_name[-4:]:
        # concatenating original file path and substituted file name and path
        file_path = dir_path + '//' + file_name
        outfile_name = '_'.join( [file_name[:-4], date, '.txt'] )
        outfile_path = dir_path + new_folder_name + outfile_name

        with open(file_path, 'r') as txt_file, \
            open(outfile_path, 'w') as out_txt_file:
            
            file_content_string = txt_file.read()
            
            for var,value in substituitions.items():
                file_content_string = sub(var, value, file_content_string)
                
            out_txt_file.write(file_content_string)

            print(f'{file_name:^40} -> {new_folder_name + outfile_name}') #{outfile_path}

print(f'{"Code run completed":=^40}')