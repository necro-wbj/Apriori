#!python3
import csv

# DictReader
f = open('test3.csv', 'r')
reader = csv.DictReader(f)

# next(reader)
for line in reader:
    print(line['A'])
    print(line['B'])
    print(line['C'])
    print('-------')

# Reader
f = open('test3.csv', 'r')
reader = csv.reader(f)

next(reader)  # 捨棄表頭
for line in reader:
    print(line[0])
    print(line[1])
    print(line[2])
    print("-------")
