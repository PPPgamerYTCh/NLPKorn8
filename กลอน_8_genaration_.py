# -*- coding: utf-8 -*-
"""กลอน 8 Genaration .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ibF9kU2--8kauQT3AMXPSLkSIP9UxwQL

ดาวน์โหลดโมดูลจาก PythaiNLP มาใช้ชื่อ Syllable_Tokenize
"""

pip install pythainlp



"""เตรียม Data Sets กลอน จาก Google Drive"""

from pythainlp.tokenize import syllable_tokenize
import json
f = open("drive/MyDrive/datakorn/ประโยค/จันทโครพ.json")
data = json.load(f)
list1 = []
for i in range(0,len(data)):
  for j in range(0,(len(data[i]['text']))):
    for k in range(0,len((data[i]['text'][j]))):
        x = syllable_tokenize(data[i]['text'][j][k])
        list1.append(x)
       
list2 = []
for i in range(0,len(list1)):
  for j in range(0,len(list1[i])):
    if list1[i][j] == '\t':
      list2.append(list1[i][j-1])
list3 = []
for i in range(0,len(list1)):
  for j in range(0,len(list1[i])):
    if list1[i][j] == '\t':
      list3.append(list1[i][j+3])
dic3 = {}
a = [5,11,14,15,20,21,22,23,26,28,34,36,40,41,43,49,55,57,62,75,82,92,96,99,
     101,103,111,113,120,123,132,134,136,137,139,145,152,157,160,162,170,173,
     176,178,180,184,186,192,208,211,214,216,217,230,231,236,241,242,246,248,249,
     250,251,252,255,256,257,258,259,260,263,264,265,270,271,278,280,284,289,291,296,
     300,302,304,307,310,312,313,316,320,323,325,326,328,332,333,335,343,346,347,348,
     355,357,361,362,378,386,388,396,400,401,404,406,408,409,413,426,433,438,444,445,446,
     448,445,455,456,464,465,468,470,473,477,479,481,482,483,485,484,497,502,508,510,515,
     516,529,530,534,543,553,562,564,570,571,573,574,575,590,595,597,598,599,606,611,613,618,
     619,620,621,622,626,628,629,632,633,635,636,640,641,642,644,645,651,669,671,672,
     674,675,676,677,678,679,682,687,691,693,698,702,704,731,736,753,756,757,758,761,762]   
for i in range(0,len(list1)):
  if i in a:
    continue
  else:
    if list2[i] not in dic3:
       dic3[list2[i]] = set()
       dic3[list2[i]].add(list3[i])
    else:
       dic3[list2[i]].add(list3[i])
       print(list2[i] , " <----> ", dic3[list2[i]], "[", i ,"]")
f = open("drive/MyDrive/datakorn/ประโยค/นิราศบางเรื่องของสุนทรภู่.json")
data1 = json.load(f)
list4 = []
b = [12,32,47,60,90,93,95,109,123,135,156,165,173,185,205,210,
     220,238,271,272,278,295,297,299,308,322,340,356,404,418,
     420,430,435,442,447,466,469,481,482,508,535,568,571,578,
     601,610,615,627,631,640,657,658,660,667,671,672,684,692,
     694,697,705,733,734,740,746,757,760,770,787,790,791,804,
     807,808,810,816,819,820,833,854,857,859,862,876,880,884,
     892,894,900,907,912,919,920,933,944,945,949,952,960,967,
     970,971,973,974,975,985,993,997,998,1011,1026,1030,1043,
     1053,1068,1076,1085,1090,1091,1101,1106,1108,1109,1123,1127]

for i in range(0,len(data1)-5):
  for j in range(0,(len(data1[i]['text']))):
    for k in range(0,len((data1[i]['text'][j]))):
        x = syllable_tokenize(data1[i]['text'][j][k])
        list4.append(x)     
list5 = []
for i in range(0,len(list4)):
  for j in range(0,len(list4[i])-1):
    if list4[i][j] == '\t':
      list5.append(list4[i][j-1])
list6 = []
for i in range(0,len(list4)):
  for j in range(0,len(list4[i])-1):
    if list4[i][j] == '\t':
      list6.append(list4[i][j+3])
for m in range(0,len(list4)-3):
  if m in b:
    continue
  else:
    if list5[m] not in dic3:
       dic3[list5[m]] = set()
       dic3[list5[m]].add(list6[m])
    else:
       dic3[list5[m]].add(list6[m]) 
       print(list5[m] , " <----> ", dic3[list5[m]], "[", 763  + m ,"]")

print(dic3)

#1. convert word to index
#2. map index to word embeddings
#3. feed word embeddings to model