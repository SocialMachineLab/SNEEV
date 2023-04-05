import torch


def jaccard(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection) / union

def editDistance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]



def semantic_similarity(a,b):
    cos = torch.nn.CosineSimilarity(dim=0,eps=1e-6)

    result=[]
    for i in a:
        ee=[]
        for j in b:
            ee.append(cos(i,j))
        result.append(mean(ee))
    semantic = sum(result)/len(result)
    return semantic