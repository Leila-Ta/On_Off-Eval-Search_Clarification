from sklearn.metrics import ndcg_score, dcg_score
import scipy.stats
import csv
from collections import defaultdict
import numpy as np
from scipy.stats import rankdata

# outcorrelation = open("./RandomRankerLong.txt", "w")
outndcg = open("./SVMNDCG.txt", "w")

for en in range (1):
    LenMyFileP = 0
    LenMyFileS = 0
    LenMyFileK = 0
    LenMyFileN = 0
    PCorr = 0.0
    PSp = 0.0
    PSpRank = 0.0
    PK = 0.0
    PKRank = 0.0
    ndcg1 = 0.0
    ndcg2 = 0.0
    ndcg3 = 0.0
    ndcgmanual1=0

    for j in range(5):
        LRank_file = open("./LTRmyScoreFileSVM"+str(j+1)+".txt")
        read_Score_file = csv.reader(LRank_file, delimiter="\t")
        Mimics = open("./HighestEngagementLevel(MIMICS-Dou).txt")
        read_Mimics=csv.reader(Mimics, delimiter="\t")
        out = open("./RankOfflineRankingMedHigh3.txt", "w")
        out1 = open("./RankEngagementMedHigh.txt", "w")

        Dict_QueryClarq= defaultdict(list)
        Dict_Main=defaultdict(list)

        x=0
        QC=0
        NewQuery = ""
        NewRank= ""
        Mai = []

        for row in read_Score_file:
            if(x==0):
                x+=1
                continue
            if(x==1):
                NewQuery=row[0]
                x+=1
            if (row[0] == NewQuery):
                Mai.append(row[2])
            else:
                Dict_QueryClarq[NewQuery] = Mai.copy()
                NewQuery = row[0]
                Mai.clear()
                Mai.append(row[2])

        Dict_QueryClarq[NewQuery] = Mai.copy()
        Mai.clear()
        if(len(Dict_QueryClarq)>0):
            for rm in read_Mimics:
                if (QC == 0):
                    QC += 1
                    continue

                if (rm[1] in Dict_QueryClarq.keys()):
                    if (QC == 1):
                        NewQuery = rm[1]
                        QC += 1

                    if(NewQuery==rm[1]):
                        Mai.append(rm[3])
                    else:
                        Dict_Main[NewQuery] = Mai.copy()
                        Mai.clear()
                        NewQuery = rm[1]
                        Mai.append(rm[3])

            if (NewQuery in Dict_QueryClarq.keys()):
                Dict_Main[NewQuery] = Mai.copy()
                Mai.clear()

        for k in Dict_QueryClarq.keys():
            list1 = []
            list2 = []
            xranks=[]

            list1 = [float(a) for a in Dict_Main[k]]
            list2 = [float(b) for b in Dict_QueryClarq[k]]

            # Calculate the rank of x's
            xranks=len(list1)+1 - rankdata(list1).astype(int)
            xranks=xranks.tolist()
            yranks = len(list2) + 1 - rankdata(list2).astype(int)
            yranks=yranks.tolist()

            for i in xranks:
                out1.write(k + '\t')
                out1.write(str(i))
                out1.write('\n')

            for i in yranks:
                out.write(k + '\t')
                out.write(str(i))
                out.write('\n')

            if(-2<scipy.stats.spearmanr(list2, list1)[0]<2):
                PSp = (scipy.stats.spearmanr(np.array(list2), np.array(list1))[0]) + PSp
                PSpRank = (scipy.stats.spearmanr(yranks, xranks)[0]) + PSpRank
                LenMyFileS += 1

            if(-2<scipy.stats.kendalltau(list2, list1)[0]<2):
                PK=(scipy.stats.kendalltau(np.array(list2), np.array(list1))[0])+PK
                PKRank = (scipy.stats.kendalltau(yranks, xranks)[0]) + PKRank
                LenMyFileK += 1

            print("here")
            print(list1)
            l2 = [val for (_, val) in sorted(zip(list2, list1), key=lambda x: x[0], reverse=True)]
            list1.sort(reverse=True)
            print(list1)
            print(list2)
            print("\nSorted List = ", l2)
            print(ndcg_score(np.asarray([list1]), np.asarray([l2]), k=1))
            ndcg1 = ndcg_score(np.asarray([list1]), np.asarray([l2]), k=1)+ndcg1
            ndcg2 = ndcg_score(np.asarray([list1]), np.asarray([l2]), k=2) + ndcg2
            ndcg3 = ndcg_score(np.asarray([list1]), np.asarray([l2]), k=3) + ndcg3
            outndcg.write(str(k)+'\t'+str(ndcg_score(np.asarray([list1]), np.asarray([l2]), k=1))+'\t'+str(ndcg_score(np.asarray([list1]), np.asarray([l2]), k=3)))
            outndcg.write('\n')

            # DCG score
            dcg = dcg_score([list1], [l2])

            # IDCG score
            idcg = dcg_score([list1], [list1])

            ndcgmanual=0

            # Normalized DCG score
            ndcgmanual = dcg / idcg
            ndcgmanual1=ndcgmanual+ndcgmanual1
            LenMyFileN+=1

    print("Kendall"+str(en+1))

    if(LenMyFileK>0):
        print(PK/LenMyFileK)
        print(PKRank / LenMyFileK)
    else:
        print("0")
    print("Spearman"+str(en+1))
    print(PSp/LenMyFileS)
    print(PSpRank / LenMyFileS)
    print("NDCG@1"+str(en+1))

    if(LenMyFileN>0):
        print(ndcg1/LenMyFileN)
        print(LenMyFileN)
    else:
        print("0")

    print("NDCG@2" + str(en + 1))

    if (LenMyFileN > 0):
        print(ndcg2 / LenMyFileN)
    else:
        print("0")

    print("NDCG@3"+str(en+1))

    if(LenMyFileN>0):
        print(LenMyFileN)
        print(ndcg3/LenMyFileN)
    else:
        print("0")
