from Functions import *
import os

ProgramDir = os.getcwd()
ParentFolderPath= 'C:\\Users\mtamanna\Desktop\Robust\Mahtab'
os.chdir(ParentFolderPath)

file = "qrels.robust2004.txt"
QID_list = []
DOCID_list = []
QueryDoc_list = []
REL_list =[]

with open(file, 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line.split(" ")[3])
        QID_list.append(line.split(" ")[0])
        QueryDoc_list.append(line.split(" ")[2])
        REL_list.append([line.split(" ")[0],line.split(" ")[2],line.split(" ")[3]])

list_Pickel(QID_list,"QID_list")
list_Pickel(QueryDoc_list,"QueryDoc_list")
list_Pickel(REL_list,"REL_list")