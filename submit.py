# CS161 project 1 submission script
# last updated: August 30, 2020
#
# best to run this in an empty directory to avoid weird errors
#
# a quick script to copy your project 1 scripts out of the VM
# for submission. directly copy-pasting out of the VM is not
# recommended because it might insert weird characters.
#
# if you want to submit only partially, simply ignore the
# password prompt for any users you want to skip with ctrl+C
#
# to create the submission manually, create the following
# directory structure: 
#
# customizer/.customization
# whistleblower/egg
# smith/egg
# hoon/interact
# brown/arg
# brown/egg
# anderson/interact
# phisher/egg
#
# and zip these folders (do not zip a single folder that
# contains all the user folders within it)

import sys
import os
from zipfile import ZipFile

# create temp folders for each user
try:
    for i in ['customizer', 'whistleblower', 'smith', 'hoon', 'brown', 'anderson', 'phisher']:
        os.mkdir(i)
except OSError:
    print('CONFLICTING FILE(S) DETECTED!')
    print('Move this script into an empty directory, and try again.')
    sys.exit()

# copy student files out of the VM
print('YOU MUST INCLUDE THE CUSTOMIZER FILE TO PASS THE AUTOGRADER!')
print('(type the password \'customizer\'.)')
os.system('scp -P 16120 customizer@127.0.0.1:~/.customization customizer')
os.system('scp -P 16120 whistleblower@127.0.0.1:~/egg whistleblower')
os.system('scp -P 16120 smith@127.0.0.1:~/egg smith')
os.system('scp -P 16120 hoon@127.0.0.1:~/interact hoon')
os.system('scp -P 16120 brown@127.0.0.1:~/\{egg,arg\} brown')
os.system('scp -P 16120 anderson@127.0.0.1:~/interact anderson')
os.system('scp -P 16120 phisher@127.0.0.1:~/egg phisher')

# zip up folders. this could be a one-line call to
# os.system, but since git bash has no zip command,
# we get to do this fun thing.
files = ['customizer/.customization', 'whistleblower/egg', 'smith/egg',
         'hoon/interact', 'brown/egg', 'brown/arg', 'anderson/interact',
         'phisher/egg']
with ZipFile('submission.zip', 'w') as z:
    for i in files:
        if os.path.exists(i):
            z.write(i)

# remove the temp user folders
os.system('rm -rf customizer whistleblower smith hoon brown anderson phisher')
print('Done! Upload submission.zip to Gradescope.')
