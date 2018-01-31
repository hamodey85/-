import os
getDirection = os.getcwd()

path = r"C:\Users\hamod\OneDrive\Desktop\one-million-arab-coders-full-stack\projects\secret msg\prank"
# getFiles = os.listdir(getDirection)
def rename_files():
    save_path = os.getcwd()  # get directory
    get_files = os.listdir(path)  # get Files from directory
    os.chdir(path) # chenge directory

    for file in get_files:
        os.rename(file, file.translate(None,'0123456789')) #change Names
    os.chdir(save_path)

rename_files()
