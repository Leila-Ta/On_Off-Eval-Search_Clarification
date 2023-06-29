import csv
from collections import defaultdict

tsv_file = open("/Mimics-ClickexploreSampling.tsv")
read_tsv = csv.reader(tsv_file, delimiter="\t")

tsv_file1 = open("/Task1-OfflineRating.tsv")
read1_tsv = csv.reader(tsv_file1, delimiter="\t")

tsv_file2 = open("/Task2-QualityLabelling.tsv")
read2_tsv = csv.reader(tsv_file2, delimiter="\t")

tsv_file3 = open("/Task3-AspectLabelling.tsv")
read3_tsv = csv.reader(tsv_file3, delimiter="\t")

#Prepare features for RankLib Application (https://sourceforge.net/p/lemur/wiki/RankLib/)
out = open("/MIMICS-ClickExplore_Aspectfeatures.txt", "w")

Dict_QueryClarq= defaultdict(dict)
Dict_QueryClarq1= defaultdict(dict)
Dict_QueryClarq2= defaultdict(dict)
Dict_QueryClarq3= defaultdict(dict)
Dict_QueryClarq4= defaultdict(dict)
Dict_QueryClarq5= defaultdict(dict)
Dict_QueryClarq6= defaultdict(dict)
qid = {}

qid_number=1
CQ=1
x=0

for row in read_tsv:
    if (x==0):
        x+=1
        continue

    if row[0] not in Dict_QueryClarq.keys():
        CQ = 1
        qid[row[0]] = qid_number
        qid_number += 1

    Dict_QueryClarq[row[0]][CQ] = row[8]
    CQ+=1

tsv_file.close()

CQ=1
x=0

for row in read1_tsv:
    if (x==0):
        x+=1
        continue

    if row[0] not in Dict_QueryClarq1.keys():
        CQ = 1

    Dict_QueryClarq1[row[0]][CQ]=row[7]
    CQ += 1

tsv_file1.close()

CQ=1
x=0

for row in read2_tsv:
    if (x==0):
        x+=1
        continue

    if row[0] not in Dict_QueryClarq2.keys():
        CQ = 1

    Dict_QueryClarq2[row[0]][CQ]=row[12]
    CQ += 1

tsv_file2.close()

CQ=1
x=0

for row in read3_tsv:
    if (x==0):
        x+=1
        continue

    if row[0] not in Dict_QueryClarq3.keys():
        CQ = 1

    Dict_QueryClarq3[row[0]][CQ]=row[7]
    Dict_QueryClarq4[row[0]][CQ]=row[8]
    Dict_QueryClarq5[row[0]][CQ]=row[9]
    Dict_QueryClarq6[row[0]][CQ]=row[10]
    CQ+=1

tsv_file3.close()

for V, K in Dict_QueryClarq.items():
    for Z, C in K.items():
        print(V)
        print(K)
        print(Z)
        print(C)
        print(Dict_QueryClarq[V][Z])
        out.write(str(Dict_QueryClarq[V][Z]) + " qid:" + str(qid[V])+" 1:" +str(Dict_QueryClarq1[V][Z])+" 2:" +str(Dict_QueryClarq2[V][Z])+" 3:" +str(Dict_QueryClarq3[V][Z])+" 4:" +str(Dict_QueryClarq4[V][Z])+" 5:" +str(Dict_QueryClarq5[V][Z])+" 6:" +str(Dict_QueryClarq6[V][Z]))
        out.write('\n')

print("Done")
out.close()