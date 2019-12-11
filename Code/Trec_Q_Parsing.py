from Functions import *
import os

file = "rb04-queries.txt"
QUERYID_list = []
QUERYTEXT_list = []

with open(file, 'r') as f:
    lines = f.readlines()
    for line in lines:
        QUERYID_list.append(line.split(":")[0])
        QUERYTEXT_list.append(line.split(":")[1])
# print(QUERYID_list)
# print(QUERYTEXT_list)

list_Pickel(QUERYID_list,"QUERYID_list")
list_Pickel(QUERYTEXT_list,"QUERYTEXT_list")
