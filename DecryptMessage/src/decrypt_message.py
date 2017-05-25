import os

def rename_files():
    saved_path = os.getcwd()
    _directory = "../photos/prank"
    os.chdir(_directory)
    for filename in os.listdir("."):
        #remove numbers
        result = ''.join([i for i in filename if not i.isdigit()])
        os.rename(filename, result)
    os.chdir(saved_path)

rename_files()