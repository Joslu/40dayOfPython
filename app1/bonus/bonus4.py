file_names = ["1.myFile1.text", "2.myFile2.txt"]

for fileName in file_names:
    fileName = fileName.replace('.', '-', 1)
    print(fileName)

