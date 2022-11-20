# txt-auto-editor
Helping Marcelo edit his .txt easily

Script looks for a .csv file in the folder where it's running from. It will assume it's comprised of lines with VARIABLES,VALUES pairs.

It will open it, ignore the first line (headers), check for a line with "folder_with_txt,_{something}_" in order to decide with folder to check for .txt files. If _{something}_ contains no characters (empty string), it will assume the folder with the .txt files is folder where the script is running from.
  
It will go through all the .txt files in that folder, changing all instances of VARIABLES by it's associated VALUE per the .csv document.
