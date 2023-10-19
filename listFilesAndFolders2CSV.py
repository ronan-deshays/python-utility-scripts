#!/usr/bin/env python

"""List recursively, in a CSV file, all files and folders contained in a directory tree"""

from pathlib import Path
from os import walk
from csv import writer

__author__ = "Ronan DESHAYS"
__license__ = "MIT"
__version__ = "1.0.1"
__status__ = "Production"

# USER PARAM
# put / instead of \ in path
path_of_the_directory = "D:/temp/MLC - Offres techniques 2023 09 10/ETF_AO_-_RFQ_unique-1208325"
filesListCSVname = "filesList.csv"
foldersListCSVname = "foldersList.csv"

# INIT
rootPath = Path(path_of_the_directory)
fileRows = [["root","file"]] # variable which stores temporarily files list before writing in csv file
folderRows = [["root","dir"]] # variable which stores temporarily folders list before writing in csv file

# LOOP
for (root,dirs,files) in walk(rootPath):

    for file in files:
        fileRows.append([root,file]) # add a data row for each file detected

    for dir in dirs:
        folderRows.append([root,dir]) # data rows of csv file

# SAVE
with open(filesListCSVname, 'w') as f:
	write = writer(f)
	write.writerows(fileRows)

with open(foldersListCSVname, 'w') as f:
	write = writer(f)
	write.writerows(folderRows)