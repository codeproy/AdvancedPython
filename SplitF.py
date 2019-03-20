import os
import shutil
import datetime
src = r'E:\Python\Split File'
#dst = r'C:\Users\partha\Documents\newPython'
fnames = os.listdir(src)


def create_dir(d):
    if not os.path.exists(d):
        os.makedirs(d)

def copy_files(f,d):
    try:
        shutil.copy(f,d)
    except:
        pass

def listdir_fullpath(d):
    return ([os.path.join(d, f) for f in os.listdir(d)])
#    print(a)

fnames = listdir_fullpath(src)


a_year = []

for eachf in fnames:

    
    #print(eachf)
    ftime = str(datetime.datetime.fromtimestamp(os.path.getmtime(eachf)))
    fyear = ftime.split('-')[0]

    d = os.path.join(src, fyear)
    if fyear in a_year:
        # copy to existing folder)
        copy_files(eachf,d)

    else:
        # creat and copy to new folder
        #d = os.path.join(src, fyear)
        create_dir(d)
        copy_files(eachf,d)
        a_year.append(fyear)

print(a_year)
    
    

