from pathlib import Path


def readfileandfolder():
    Path = Path('')
    items = list(Path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i + 1} : {items}")


def createfile():
    readfileandfolder()


print("press 1 to create a file ")
print("press 2 to Read a file ")
print("press 3 to Update a file ")
print("press 4 to delete a file ")

check = int(input("Please tell what you wanna do "))

if check == 1:
    createfile()