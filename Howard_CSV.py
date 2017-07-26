import pprint
from pymongo import MongoClient
import csv
import subprocess
import os

client = MongoClient()

# Howard_TimeLog

db_log = client.mydb
collection_log = db_log.groupLog
file=open("log.txt", "w")

for post_log in collection_log.find({"uidWell":"Howard4H-1","uidLog":"TimeLog"},{"curvInfoList.mnemonic":1,'_id': False}):
   pprint.pprint(post_log)
   s = str(post_log)
   file.write(s + "\n")
file.close()

infile = "log.txt"
outfile = "trim_log.txt"

delete_list = ["{","}","mnemonic",":","'","curvInfoList",'[',']', " "]
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()

with open('trim_log.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('Howard4H-1_TimeLog_log.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(lines)


db_data = client.mydb
collection_data = db_data.data
file=open("data.txt", "w")

for post_log in collection_data.find({"uidWell":"Howard4H-1","uidLog":"TimeLog"},{"data":1,'_id': False}):
   pprint.pprint(post_log)
   s = str(post_log)
   file.write(s + "\n")
file.close()

infile = "data.txt"
outfile = "trim_data.txt"

delete_list = ["{","}",":","'","data",'[',']', " "]
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()

with open('trim_data.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('Howard4H-1_TimeLog_data.csv', 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerows(lines)

file_object = open('Howard4H-1_TimeLog_data.csv', 'r')
lines = csv.reader(file_object, delimiter=',', quotechar='"')
flag = 0
data=[]
for line in lines:
  if line == []:
     flag =1
     continue
  else:
     data.append(line)
file_object.close()
if flag ==1:
        file_object = open('Howard4H-1_TimeLog_data.csv', 'w')
        for line in data:
            str1 = ','.join(line)
            file_object.write(str1+"\n")
file_object.close()


subprocess.call("type Howard4H-1_TimeLog_log.csv Howard4H-1_TimeLog_data.csv > Howard4H-1_TimeLog_1.csv", shell=True)
os.remove("trim_data.txt")
os.remove("trim_log.txt")
os.remove("data.txt")
os.remove("log.txt")
os.remove("Howard4H-1_TimeLog_log.csv")
os.remove("Howard4H-1_TimeLog_data.csv")

with open('Howard4H-1_TimeLog_1.csv') as infile, open('Howard4H-1_TimeLog.csv', 'w') as outfile:
    for line in infile:
        if not line.strip(): continue
        outfile.write(line)

os.remove("Howard4H-1_TimeLog_1.csv")
subprocess.call("move Howard4H-1_TimeLog.csv C:\\Users\AM0C70368\python_projects\CSV\Well\Howard4H-1", shell =True)


#Howard_MudLog

db_log = client.mydb
collection_log = db_log.groupLog
file=open("log.txt", "w")

for post_log in collection_log.find({"uidWell":"Howard4H-1","uidLog":"MudLog"},{"curvInfoList.mnemonic":1,'_id': False}):
   pprint.pprint(post_log)
   s = str(post_log)
   file.write(s + "\n")
file.close()

infile = "log.txt"
outfile = "trim_log.txt"

delete_list = ["{","}","mnemonic",":","'","curvInfoList",'[',']', " "]
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()

with open('trim_log.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('Howard4H-1_MudLog_log.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(lines)

db_data = client.mydb
collection_data = db_data.data
file=open("data.txt", "w")

for post_log in collection_data.find({"uidWell":"Howard4H-1","uidLog":"MudLog"},{"data":1,'_id': False}):
   pprint.pprint(post_log)
   s = str(post_log)
   file.write(s + "\n")
file.close()

infile = "data.txt"
outfile = "trim_data.txt"

delete_list = ["{","}",":","'","data",'[',']', " "]
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()

with open('trim_data.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('Howard4H-1_MudLog_data.csv', 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerows(lines)

file_object = open('Howard4H-1_MudLog_data.csv', 'r')
lines = csv.reader(file_object, delimiter=',', quotechar='"')
flag = 0
data=[]
for line in lines:
  if line == []:
     flag =1
     continue
  else:
     data.append(line)
file_object.close()
if flag ==1:
        file_object = open('Howard4H-1_MudLog_data.csv', 'w')
        for line in data:
            str1 = ','.join(line)
            file_object.write(str1+"\n")
file_object.close()

subprocess.call("type Howard4H-1_MudLog_log.csv Howard4H-1_MudLog_data.csv > Howard4H-1_MudLog_1.csv", shell=True)
os.remove("trim_data.txt")
os.remove("trim_log.txt")
os.remove("data.txt")
os.remove("log.txt")
os.remove("Howard4H-1_MudLog_log.csv")
os.remove("Howard4H-1_MudLog_data.csv")

with open('Howard4H-1_MudLog_1.csv') as infile, open('Howard4H-1_MudLog.csv', 'w') as outfile:
    for line in infile:
        if not line.strip(): continue
        outfile.write(line)

os.remove("Howard4H-1_MudLog_1.csv")
subprocess.call("move Howard4H-1_MudLog.csv C:\\Users\AM0C70368\python_projects\CSV\Well\Howard4H-1", shell =True)

#DepthLog_Howard

db_log = client.mydb
collection_log = db_log.groupLog
file=open("log.txt", "w")

for post_log in collection_log.find({"uidWell":"Howard4H-1","uidLog":"DepthLog"},{"curvInfoList.mnemonic":1,'_id': False}):
   pprint.pprint(post_log)
   s = str(post_log)
   file.write(s + "\n")
file.close()

infile = "log.txt"
outfile = "trim_log.txt"

delete_list = ["{","}","mnemonic",":","'","curvInfoList",'[',']', " "]
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()

with open('trim_log.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('Howard4H-1_DepthLog_log.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(lines)

db_data = client.mydb
collection_data = db_data.data
file=open("data.txt", "w")

for post_log in collection_data.find({"uidWell":"Howard4H-1","uidLog":"DepthLog"},{"data":1,'_id': False}):
   pprint.pprint(post_log)
   s = str(post_log)
   file.write(s + "\n")
file.close()

infile = "data.txt"
outfile = "trim_data.txt"

delete_list = ["{","}",":","'","data",'[',']',]
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()

with open('trim_data.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('Howard4H-1_DepthLog_data.csv', 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerows(lines)

file_object = open('Howard4H-1_DepthLog_data.csv', 'r')
lines = csv.reader(file_object, delimiter=',', quotechar='"')
flag = 0
data=[]
for line in lines:
  if line == []:
     flag =1
     continue
  else:
     data.append(line)
file_object.close()
if flag ==1:
        file_object = open('Howard4H-1_DepthLog_data.csv', 'w')
        for line in data:
            str1 = ','.join(line)
            file_object.write(str1+"\n")
file_object.close()

subprocess.call("type Howard4H-1_DepthLog_log.csv Howard4H-1_DepthLog_data.csv > Howard4H-1_DepthLog_1.csv", shell=True)
os.remove("trim_data.txt")
os.remove("trim_log.txt")
os.remove("data.txt")
os.remove("log.txt")
os.remove("Howard4H-1_DepthLog_log.csv")
os.remove("Howard4H-1_DepthLog_data.csv")

with open('Howard4H-1_DepthLog_1.csv') as infile, open('Howard4H-1_DepthLog.csv', 'w') as outfile:
    for line in infile:
        if not line.strip(): continue
        outfile.write(line)

os.remove("Howard4H-1_DepthLog_1.csv")

subprocess.call("move Howard4H-1_DepthLog.csv C:\\Users\AM0C70368\python_projects\CSV\Well\Howard4H-1", shell =True)

