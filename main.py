import requests

print("Note: \n\tThe URL should start with 'http://' or 'https://' or it will be taken as local directory path.")

file1 = input("Enter URL/Local Path of first file: ")
format1 = input("Enter 1 if first file format is line and 2 if file format is table: ")
file2 = input("Enter URL/Local Path of second file: ")
format2 = input("Enter 1 if second file format is line and 2 if file format is table: ")

try:
    if (file1[:7] == "http://" or file1[:7] == "HTTP://" or file1[:8] == "https://" or file1[:8] == "HTTPS://"):
        data1 = requests.get(file1).text
    else:
        f = open(file1, 'r')
        data1 = f.read()
        f.close()
    if (file2[:7] == "http://" or file2[:7] == "HTTP://" or file2[:8] == "https://" or file2[:8] == "HTTPS://"):
        data2 = requests.get(file2).text
    else:
        f = open(file2, 'r')
        data2 = f.read()
        f.close()
except Exception as e:
    print("Invalid Input")


def textToList(fileData, fileFormat):
    try:
        if (int(fileFormat) == 1):
            fileData = fileData.split(' ')
            rows = fileData[0]
            data = fileData[1:]
            cols = len(data) / int(rows)
            dataList = []
            temp = []
            counter = 1
            for ele in data:
                if (counter == int(cols)):
                    temp.append(ele)
                    dataList.append(temp)
                    counter = 1
                    temp = []
                else:
                    temp.append(ele)
                    counter += 1
            return dataList

        if (int(fileFormat) == 2):
            fileData = fileData.split('\n')
            dataList = []
            for row in fileData:
                row = row.split(' ')
                row = list(filter(None, row))
                dataList.append(row)
            return dataList

        else:
            print('Invalid file format Input.')
    except:
        print('Invalid file format Input.')


def append(file1, file2):
    print("Appended output: ")
    if (len(file1[0]) == len(file2[0])):
        for row in file1:
            for ele in row:
                print(ele + "\t", end='')
            print('')
        for row in file2:
            for ele in row:
                print(ele + '\t', end='')
            print('')
        basic()
    else:
        print("Files format is not compatible for append operation.")
        basic()


def combine(file1, file2):
    print("Combined output: ")
    if (len(file1) == len(file2)):
        for i in range(len(file1)):
            for ele in file1[i]:
                print(ele + "\t", end="")
            for ele in file2[i]:
                print(ele + "\t", end="")
            print('')
        basic()
    else:
        print("Files format is not compatible for combine operation.")
        basic()


def sumFiles(file1, file2):
    print("Sum output: ")
    if (len(file1) == len(file2) and len(file1[0]) == len(file2[0])):
        for i in range(len(file1)):
            for j in range(len(file1[i])):
                print(str(int(file1[i][j]) + int(file2[i][j])) + "\t", end='')
            print('')
        basic()
    else:
        print("Files format is not compatible for sum operation.")
        basic()


def basic():
    operation = input("""
Select the operation 
1. Enter 1 for APPEND operation
2. Enter 2 for COMBINE operation
3. Enter 3 for SUM operation
4. Enter -1 to EXIT
Selection(1-3): """)
    try:
        if (int(operation) == 1):
            append(textToList(data1, format1), textToList(data2, format2))
        if (int(operation) == 2):
            combine(textToList(data1, format1), textToList(data2, format2))
        if (int(operation) == 3):
            sumFiles(textToList(data1, format1), textToList(data2, format2))
        if (int(operation) == -1):
            pass
        else:
            print("Invalid Input")
    except:
        print("Invalid Input")
        basic()


basic()
