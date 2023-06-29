from sklearn.metrics import ndcg_score, dcg_score
import csv
from collections import defaultdict

for en in range (1):
    LenMyFileN = 0
    ndcg = 0.0
    x=0
    NewQuery = ""
    Mai = defaultdict(list)
    Score_Rel = defaultdict(list)

    for j in range(5):
        LRank_file = open("/Users/leila/PhD/Clarifying Question/Manual/RandomRanker/RandomRanker"+str(j+1)+".txt")
        read_Score_file = csv.reader(LRank_file, delimiter="\t")
        Mimics = open("/Users/leila/PhD/Clarifying Question/Manual/HighestEngagementLevel(MIMICS-Manual).txt")
        read_Mimics=csv.reader(Mimics, delimiter="\t")

        x = 0
        NewQuery = ""
        Score_Rel.clear()

        for row in read_Score_file:
            if (x == 0):
                x += 1
                continue

            if (row[0] == NewQuery):
                Score_Rel[NewQuery].append(float(row[2]))
            else:

                NewQuery = row[0]
                Score_Rel[NewQuery].append(float(row[2]))

        x=0
        NewQuery = ""
        Mai.clear()

        for rr in read_Mimics:
            if (x == 0):
                x += 1
                continue

            if (rr[1] == NewQuery):
                Mai[NewQuery].append(float(rr[3]))
            else:
                NewQuery = rr[1]
                Mai[NewQuery].append(float(rr[3]))

        for k in Score_Rel.keys():
            if (Mai[k]):
                ndcg = ndcg_score([Mai[k]], [Score_Rel[k]])+ndcg

                #DCG score
                dcg = dcg_score([Mai[k]], [Score_Rel[k]])

                # IDCG score
                idcg = dcg_score([Mai[k]], [Mai[k]])

                ndcgmanual=0
                LenMyFileN+=1
            else:
                continue

    print("NDCG"+str(en))
    if(LenMyFileN>0):
        print(ndcg/LenMyFileN)
    else:
        print("0")
