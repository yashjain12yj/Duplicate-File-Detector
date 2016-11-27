import os
import hashlib
# Open a file
path = input("Enter the path of the folder : ")
filenames = os.listdir(path)
a=[]
# This would access the files and directories
for file_ in filenames:
  os.chdir(path)
  #fo = open(str(file_),"rb")
  #print(file_,end=" : ")
  #print(hashfile(str(file_)))
  if os.path.isdir(file_):
    #If the selected file is a folder
    print("Folder" + file_)
  else:
    hash=hashlib.md5(open(str(file_),'rb').read()).hexdigest()
    if hash in a:
      print("Duplicated File Detected : "+str(file_))
      print("Deleting Duplicated File...")
      os.remove(str(file_))
      #to delete file
      print("Duplicated File Deleted.")
      print("")
      print("")
      print("")
      print("")
    else:
      a.append(hash)