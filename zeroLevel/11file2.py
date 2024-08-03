"""Different operation on file and CSV library for reading content from csv file """
# fileName = 'demo.txt'
# fileMode = 'r'
# file = open(fileName,fileMode)
# first = file.readline()
# print(first)
# second  = file.readline()
# print(second)

# file.close()
# import csv
# with open('demo.txt','r') as allRows:
#     all = csv.reader(allRows)
#     for value in all:
#         print('/'.join(value))
#         for val in value:
#             print(val)
# import csv
# with open('guest.txt','r') as guest:
#     name = csv.reader(guest)
#     for allName in name:
#         print(','.join(allName)) 
fileName = "demo.txt"
with open (fileName,'w') as file:
    del(file)
        