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
        print(os.path.join,("/PyDrill", file,))


path = 'D:\PyDrill'
name_list = os.listdir(path)
full_list = [os.path.join(path,i) for i in name_list]
time_sorted_list = sorted(full_list, key=os.path.getmtime)

print (time_sorted_list)
