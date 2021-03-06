# coding=utf-8
import sys
import re
import os

# original directory
iDirectory = '../../tmp/lm_pyss/'
# objective directory
oDirectory = '../../tmp/lm_pyvs/'
# backup directory
bDirectory = '../../tmp/backup/'
if os.path.exists(iDirectory):
    print('Loading...')
    # rescutive
    for file_or_folder in os.listdir(iDirectory):
        # generate full file path which to be treated
        pys_file_path = os.path.join(iDirectory, file_or_folder)
        # generate full file path which to save the new file generated.
        name_extension = str(file_or_folder).split('.')
        name = str(name_extension[0])
        destination_file_path = os.path.join(oDirectory, name + '.pyv') 
        # judge wheather one object in the directory is a file.
        if os.path.isfile(pys_file_path):
            # execute statement.
            os.system("python pinyinStandard2Variant.py " + file_or_folder)
            # execute backcup and clean operations
            os.system("cp " + pys_file_path +" " + bDirectory)
else:
    print('Wrong path!')

print('---------------------------------------')
print('Executing ...\n')
print('Congratuation, all the files in directory <PYSs> have been transformed into ' + oDirectory +' directory.')
print('---------------------------------------')
