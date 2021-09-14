import time
import os
import shutil

def main () :
    deletedFolderCount = 0
    deletedFileCount = 0
    path = 'C:/Users/vansh/WhitehatJR project VSC/Project Python 97/txt'
    days = 10
    seconds = time.time()-(days*24*60*60)

    if os.path.exists(path) :
        for rootFolder,folders,files in os.walk(path) :
            if seconds>=getFileorFolderAge(rootFolder) :
                removeFolder(rootFolder)
                deletedFolderCount +=1
                break

            else :
                for folder in folders :
                    folderPath = os.path.join(rootFolder,folder)
                    if seconds>=getFileorFolderAge(folderPath) :
                        removeFolder(rootFolder)
                        deletedFolderCount+=1
                for file in files :
                    filePath = os.path.join(rootFolder,file)
                    if seconds>=getFileorFolderAge(filePath) :
                        removeFile(rootFolder)
                        deletedFileCount+=1

        
        else :
            if seconds>=getFileorFolderAge(path) :
                removeFile(path)
                deletedFileCount +=1
                     
    else : 
        print(f'"{path}" is not found')
    print(f"Total folders deleted :  {deletedFolderCount}")
    print(f"Total files deleted :  {deletedFileCount}")                   

def removeFolder (path) :
    if not shutil.rmtree(path) :
        print(f"{path} is removed successfully!")
    
    else :
        print(f"Unable to delete the {path}")

def removeFile (path) :
    if not os.remove(path) :
        print(f"{path} is removed successfully!")
    
    else :
        print(f"Unable to delete the {path}")

def getFileorFolderAge (path) :
    ctime = os.stat(path).st_ctime
    return ctime

main()

