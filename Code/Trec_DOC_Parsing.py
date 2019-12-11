import xml.etree.ElementTree as ElementTree
import os
from Functions import *

ProgramDir = os.getcwd()
ParentFolderPath= 'C:\\Users\mtamanna\Desktop\Robust\Mahtab\FT_ALL'
os.chdir(ParentFolderPath)
files = os.listdir(ParentFolderPath)

DOCNUM_list = []
DOCTEXT_list = []

for file in files:
    try:
        with open(file, 'r') as f:
            xml = f.read()
        xml = '<ROOT>' + xml + '</ROOT>'
        root = ElementTree.fromstring(xml)
        for doc in root:
            DOCNUM_list.append(doc.find('DOCNO').text.strip())
            DOCTEXT_list.append(doc.find('TEXT').text.strip())
    except:
        print(str(file))

list_Pickel(DOCNUM_list,"DOCNUM_list")
list_Pickel(DOCTEXT_list,"DOCTEXT_list")

