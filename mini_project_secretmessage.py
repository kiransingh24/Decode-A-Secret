import os
def rename_files():
    #print file names in the directory E:\python_projects\alphabet
    file_list = os.listdir(r"E:\python_projects\alphabet")
    print(file_list)
    file_loc = os.getcwd()
    print(file_loc)
    curr_dir = os.chdir(r"E:\python_projects\alphabet")
    print(curr_dir)
    #Rename files and decode the secret message
    for file_name in file_list:
       os.rename(file_name,file_name.translate(None, "0123456789"))
    os.chdir(file_loc)
rename_files()
