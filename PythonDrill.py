import os

files = os.listdir('D:\\PyDrill')
print(files)

fName = 'drill4.txt'

fPath = 'D:\\PyDrill\\'

abPath = os.path.join(fPath, fName)

print(abPath)

time = os.path.getmtime('D:\PyDrill\drill4.txt')
print(time)

for file in os.listdir('D:\\PyDrill\\'):
    if file.endswith(".txt"):
        print(os.path.join("/PyDrill", file,))





