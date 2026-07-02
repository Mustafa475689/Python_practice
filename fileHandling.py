import os
from pathlib import Path
    
    # Function for file and folder paths
def readfileandfolder():
        path = Path('')
        items = list(path.rglob('*'))
        for i, items in enumerate(items):
            print(f"{i + 1} : {items}")

    # Function to create file
def createfile():
        try:
            readfileandfolder()
            name = input("Please write your file name: ")
            p = Path(name)
            if not p.exists():
                with open(p, "w") as fs:
                    data = input("What you wanna write in this file: ")
                    fs.write(data)
            
                print(f"File Created successfully: ")
            else:   
                print("This name of file is already exists")

        except Exception as err:
            print(f"An error occured as {err}")

    # Function to Read the creted files
def readfile():
        try:
            readfileandfolder()
            name = input("Which file you wanna read write the name here: ")
            p = Path(name)

            if p.exists() and p.is_file():
                with open(p, "r") as fs:
                    data = fs.read()
                    print(data)
            
                print("Readed Successfully :) ")
        
            else:
                print("File do not exist :( ")

        except Exception as err:
            print(f"An error occurs as {err}")

    # Function to Read the creted files
def updatefile():
        try:
            readfileandfolder()
            name = input("Write the file name you wanna update: ")
            p = Path(name)
            if p.exists() and p.is_file():
                print("press 1 to change the name of your created  file ")
                print("press 2 to overwrite the data of your file ")
                print("press 3 to appending some content in your file ")

                res = int(input("Tell your response: "))

                if res == 1: 
                    name2 = input("Write the new name for your file")
                    p2 = Path(name2)
                    p.rename(p2)
                    print("The file name is changed successflly :) ")

                elif res == 2: 
                    with open(p, 'w') as fs:
                        data = input("Write anything to overwrite the file")
                        fs.write(data)
                        print("The file is overwritten successflly :) ")

                elif res == 3: 
                    with open(p, 'a') as fs:
                        data = input("Write anything to overwrite the file")
                        fs.write(" "  +data)
                        print("The data appended in this file :) ")

                else:
                    print("Invalid choice.")

        except Exception as err:
            print(f"An error occurs as {err}")

# Function to delete file 
def deletefile():
        try:
            readfileandfolder()
            name = input("Write the file name you wanna update: ")
            p = Path(name)
                
            if p.exists() and p.is_file():
                os.remove(name)

                print("File is removed")
            
            else:
                print("no such file exists")
        
        except Exception as err:
            print(f"An error occur as {err}")

    # System outputs 
print("press 1 to create a file ")
print("press 2 to Read a file ")
print("press 3 to Update a file ")
print("press 4 to delete a file ")

check = int(input("Please tell what you wanna do "))

if check == 1:
        createfile()
        
if check == 2:
        readfile()

if check == 3:
        updatefile()

if check == 4:
        deletefile()
