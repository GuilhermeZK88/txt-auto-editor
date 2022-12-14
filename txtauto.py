import os #listdir, path.exists, makedirs, getcwd, mkdir
from datetime import datetime
from csv import reader
from re import sub
from sys import exit

# Assuming the .csv info file is in the directory of this script
dir_path = os.getcwd()
print(f'Searching CSV file in: {dir_path}')

date = str(datetime.now())[:10]
no_csv = True

file_list = os.listdir(dir_path)
# Searching for csv file, to extract VARIABLE,VALUE pairs information for substituition
for file_name in file_list:
    if '.csv' in file_name:
        no_csv = False
        print(f'Using info from file: {file_name}')

        file_path = dir_path + '\\' + file_name
        with open(file_path) as csv_file:
            # Reading file
            reading_csv = reader(csv_file)
            # Skiping first row (column names)
            next(reading_csv)
            # Creating dictionary with VARIABLE,VALUE pairs
            substituitions = dict((row[0],row[1]) for row in reading_csv)

            for var, value in substituitions.items():
                print(f'{var:^30} -> {value}')
            # Looking for folder containing .txt files to auto substitute
            try:
                # If no folder path is given, assumes this script folder
                if substituitions['folder_with_txt'] == '':
                    print(f'Assuming .txt files are in the same folder as this script: {dir_path}.')
                    file_list.remove(file_name)
                # If a folder path is given, try acessing it
                else:
                    try:
                        # List files inside the folder
                        print('Looking the .csv for a folder path indication, where the .txt files search should happen.')
                        dir_path = substituitions['folder_with_txt']
                        file_list = os.listdir(dir_path)
                    except FileNotFoundError as e:
                        print(f"{e}. Check .csv file: {file_name} for mistakes in the folder_with_txt VARIABLE's associated VALUE: {dir_path}.")
                        sys.exit(1) #breaking execution
            except KeyError as e:
                print(f'KeyError: Could not find a VARIABLE named exactly {e} in th .csv file: {file_name}.', end=' ')
                print(f'MOVING ON: Assuming the .txt files are in the same folder as this script: {dir_path}')

            substituitions.pop('folder_with_txt')

        # Found a .csv, and got its info. Stopping further search.
        break

# Checking for .csv instructions/variables file
if no_csv:
    raise ValueError('Found no .csv file!')

# If output folder still doesn't exists, creating it
try:
    new_folder_name = '\AutoTxtEditor ' + date + '\\'
    outfile_folder_path = dir_path + new_folder_name
    os.mkdir(outfile_folder_path)
    print(f'Creating new folder: {new_folder_name}')
except FileExistsError:
    print(f"Updating {new_folder_name} folder's content.")
    pass

print(f'Searching TXT files in: {dir_path}')

for file_name in file_list:

    if '.txt' in file_name[-4:]:
        # Creating file_name and path
        file_path = dir_path + '\\' + file_name
        outfile_name = '_'.join( [file_name[:-4], date, '.txt'] )
        outfile_path = dir_path + new_folder_name + outfile_name
        # Opening files
        with open(file_path, 'r') as txt_file, \
            open(outfile_path, 'w') as out_txt_file:
            # Reading original file
            file_content_string = txt_file.read()
            # Substituing variables by it's intended value as VAR,VALUE pairs
            for var,value in substituitions.items():
                file_content_string = sub(var, value, file_content_string)

            out_txt_file.write(file_content_string)

            print(f'{file_name:^30} -> {new_folder_name + outfile_name}') #{outfile_path}

print(f'{"<CODE RUN COMPLETED!>":=^50}')