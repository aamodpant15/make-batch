**make_batch.py** is a program used to make a batch file for other .py programs, in Windows.

Batch files allow you to press `Windows+R`, enter batch file name, and execute the program attached to that batch file. This takes away the need to navigate to the python file from the terminal (if it's not already in the home folder). 

The other alternative is to add the path of the `.py` file in the [path environement variable] (https://stackoverflow.com/questions/44272416/how-to-add-a-folder-to-path-environment-variable-in-windows-10-with-screensho) in windows. But the batch file can be edited in the future to run multiple `.py` files, in order.

Usage:
1. Change the code to put the path where you want to save your batch file, and the home folder or the `.py` files.
2. In cmd, enter- `make_batch <batch-file-name>`
3. Will ask option if pause command is needed in the batch file, choose which you want (y/n)
