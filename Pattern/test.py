import pprint
from pymongo import MongoClient
import csv
import subprocess
import os

client = MongoClient()

#EGFD_WO_1_TimeLog

db_log = client.mydb
collection_log = db_log.groupLog
file=open("log.txt", "w")

for post_log in collection_log.find({"uidWell":"EGFD_WO_1","uidLog":"TimeLog"},{"curvInfoList.mnemonic":1,'_id': False}):
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
    with open('EGFD_WO_1_TimeLog_log.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(lines)


#for fetching data from mongodb collection
db_data = client.mydb
collection_data = db_data.data
file=open("data.txt", "w")

for post_log in collection_data.find({"uidWell":"EGFD_WO_1","uidLog":"TimeLog"},{"data":1,'_id': False}):
   pprint.pprint(post_log)
   s = str(post_log)
   file.write(s + "\n")
file.close()

infile = "data.txt"
outfile = "trim_data.txt"

delete_list = ["{","}",":","'","data",'[',']'," "]
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
    with open('EGFD_WO_1_TimeLog_data.csv', 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerows(lines)

file_object = open('EGFD_WO_1_TimeLog_data.csv', 'r')
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
        file_object = open('EGFD_WO_1_TimeLog_data.csv', 'w')
        for line in data:
            str1 = ','.join(line)
            file_object.write(str1+"\n")
file_object.close()


subprocess.call("type EGFD_WO_1_TimeLog_log.csv EGFD_WO_1_TimeLog_data.csv > EGFD_WO_1_TimeLog_1.csv", shell=True)
os.remove("trim_data.txt")
os.remove("trim_log.txt")
os.remove("data.txt")
os.remove("log.txt")
os.remove("EGFD_WO_1_TimeLog_log.csv")
os.remove("EGFD_WO_1_TimeLog_data.csv")



with open('C:\\Users\AM0C70368\python_projects\Pattern\EGFD_WO_1_TimeLog_1.csv') as infile, open('EGFD_WO_1_TimeLog.csv', 'w') as outfile:
    for line in infile:
        if not line.strip(): continue
        outfile.write(line)

os.remove("EGFD_WO_1_TimeLog_1.csv")