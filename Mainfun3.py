import Mainfun2

print("file1 __name__ = %s" %__name__)

if __name__ == "__main__":
    print('File2 is being run direclty')
else:
    print('File2 is beign imported')