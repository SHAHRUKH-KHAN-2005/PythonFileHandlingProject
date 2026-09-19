from pathlib import Path
import os


def showFilesAndFolder():
    path=Path("")
    items=list(path.rglob("*"))
    for i,items in  enumerate(items):
        print(f"{i+1} : {items} ")



def createFile():
    try:
        showFilesAndFolder()

        fileName=input("enter the file name you want to create:-")
        path=Path(fileName)
        if not path.exists():
            with open(path,"w") as f:
                data=input("enter the data you want to add in a file::")
                f.write(data)
                                 
            print("FILE CREATED SUCCESSFULLY")

        else:
            print("File already exists")

    except Exception as err:
        print(f"An error occured as {err}")



def readFile():
    try:
        showFilesAndFolder()

        file=input("enter the file you want to read:-")
        path=Path(file)

        if path.exists() and path.is_file():
            with open(path,"r") as f:
                data=f.read()
                print(data)
            print("FILE READED SUCCESSFULLY")

        else:
            print("File does not exists")

    except Exception as err:
        print(f"an error occured as {err}")


def updateFile():
    try:
        showFilesAndFolder()

        file=input("Enter the file you want to update::")
        path=Path(file)
        if path.exists() and path.is_file():
            print("Press 1 for rename the file name:-")
            print("Press 2 for overwriting the data into a file:-")
            print("Press 3 for appending into the file:-")

            res=int(input("enter your response:-"))

            if res==1:
                newFileName=input("Enter your new file name:-")
                path2=Path(newFileName)
                path.rename(path2)

            if res==2:
                with open(path,"w") as f:
                    data=input("Enter the data you want to overwrite in a file::")
                    f.write(data)

            if res==3:
                with open(path,"a") as f:
                    data=input("Enter the data you want to append::")
                    f.write(" "+data)

    except Exception as err:
        print(f"An error occured as {err}")


def deleteFile():
    try:
        showFilesAndFolder()

        fileName=input("Enter the file you want to delete:-")
        path=Path(fileName)

        if path.exists and path.is_file():
            os.remove(fileName)

            print("FILE DELETED SUCCESSFULLY")

    except Exception as err:
        print(f"An error occured as {err}")






print("Press 1 for writing into a file")
print("Press 2 for reading  a file")
print("Press 3 for updating  into a file")
print("Press 4 for deleting a file")

choice=int(input("enter your choice:-"))

if choice==1:
    createFile()

if choice==2:
    readFile()

if choice==3:
    updateFile()

if choice==4:
    deleteFile()


