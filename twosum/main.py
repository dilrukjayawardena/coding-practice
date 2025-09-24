from collections import defaultdict
nums = [2,5,1,7,4]
target = 6
#bf approach
def twos(nums,target):
    for i,num in enumerate(nums):
        if target-num in nums[i:]:
            print(f'{num},{target-num}')

# print(twos(nums,target))

#optimal using hash map
def twosum(nums,target):
    hmap=defaultdict(int)
    for i,num in enumerate(nums):
        if target-num in hmap:
            print(f'{num},{target-num}')
        else:
            hmap[num]=i

twosum(nums,target)
