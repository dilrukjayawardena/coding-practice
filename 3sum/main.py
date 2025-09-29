nums=[-5,3,-5,0,1,0,-1,2,5]
k=0
nums.sort()

right=len(nums)-1
ans=[]
for i,num in enumerate(nums):
    left=i+1
    if len(nums)-1>i and num == nums[i+1]:
        continue
    else:
        while left<right:
            if nums[left]+nums[right]== num*-1:
                ans.append((num,nums[left],nums[right]))
                break
            elif nums[left]+nums[right]> num*-1:
                right -= 1
            elif nums[left]+nums[right]< num*-1: 
                left += 1   

print(ans)
