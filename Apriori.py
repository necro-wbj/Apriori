#!python3
import requests
import csv
from apyori import apriori


def read_file():
    html = requests.get('https://fili.tw/pub/sample2.csv').text
    # htttps://fili.tw/pub/sample.csv
    # file = open('test.txt', 'r')
    reader = csv.reader(html.split('\n'))
    for line in reader:
        yield line


def load_data_from_file(filename):
    f = open(filename, 'r')
    for line in csv.reader(f, delimiter='\t'):
        yield line


def load_data_from_web(url):
    html = requests.get(url).text
    for line in csv.reader(html.split('\n'), delimiter='\t'):
        yield line


data = list(load_data_from_web('https://fili.tw/slide_fs/dm/sample1.csv'))
# result = apriori(data)
result = apriori(data, min_support=0.3, min_confidence=0.6)
for its in result:
    print(*list(its.items), its.support)
    for oi in its.ordered_statistics:
        print("	", *list(oi.items_base), "-->", *
              list(oi.items_add), "	", oi.confidence)
# print(data,*list(result))
