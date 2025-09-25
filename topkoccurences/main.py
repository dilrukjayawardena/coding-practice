
from collections import defaultdict, deque, Counter
import heapq
arr=[1,2,2,1,1,3,3,4,4,4,5,6]
k=3
def topkoc(arr,k):
    hmap=defaultdict(int)
    itemsque= deque(maxlen=k)
    for num in arr:
        if num in hmap:
            hmap[num] += 1
        else:
            hmap[num]=1
    print(hmap)

    for key,value in hmap.items():
        if not itemsque:
            itemsque.append((key,value))
            continue
        if itemsque[0][1]<value:
            itemsque.append((key,value))
        elif itemsque[0][1]==value:
            item=itemsque.popleft()
            itemsque.appendleft(((item[0],key),value))
        elif len(itemsque)<k:
            itemsque.appendleft((key,value))
        print(itemsque)   
    print(itemsque)

def topkoc1(arr,k):
    counts=Counter(arr)

    print(counts.most_common(k))

def topkoc2(arr,k):
    counts=Counter(arr)

    print(heapq.nlargest(k,counts,key=counts.get))

topkoc2(arr,k)

       

