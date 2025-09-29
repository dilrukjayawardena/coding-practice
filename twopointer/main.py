#two sum for sorted array
arr=[1,2,3,4,5]
target=5

def twosum(arr,target):
    n = len(arr)
    left=0
    right= n-1
    finalresult=[]
    while left<right:
        
        sum = arr[left]+arr[right]
        if target == sum:
            finalresult.append((left,right))
            left+=1
        if sum<target:
            print(left)
            left+=1
        if sum>target:
            print(right)
            right-=1
    return finalresult

# print(twosum(arr,target))

# remove given element from array

arr2 = [1,2,3,4,2,1,2]
k = 2

def remove_ele(arr,ele):
    k=0
    for i in range(len(arr)):
        if arr[i]!=ele:
            arr[k]=arr[i]
            k += 1
    while k<len(arr):
        arr[k]='_'
        k+=1

    return arr

#print(remove_ele(arr2,k))

#shift element in array
arr3 = [1,0,3,2,0,1]
ele = 0

def shift_ele(arr,ele):
    k = 0
    for i in range(len(arr)):
        if arr[i]!=ele:
            arr[k],arr[i]=arr[i],arr[k]
            k += 1
    return arr
# print(shift_ele(arr3,ele))

text = 'kama kanawada oya'

def reverse_str_with_spaces(text):
    left = 0
    right = len(text)-1
    result = [0]*len(text)
    while left<=right:
        if text[left] ==' ':
            result[left]=' '
            left += 1
            
        if text[right] ==' ':
            result[right]=' '
            right -=1
        
        if text[left] !=' ' and text[right] !=' ':
            print('1')
            result[left]=text[right]
            result[right]= text[left]
            left += 1
            right -=1
    return result

# print(reverse_str_with_spaces(text))
nums=[2,2,3,4]
def triangleNumber(nums) -> int:
    nums=sorted(nums)
    count=0
    for i in range(len(nums)):
        left=i+1
        right=i+2 
        while right<len(nums):
            if nums[i]+nums[left]>nums[right]:
                count +=1
                right +=1
            # elif nums[i]+nums[left]<nums[right]:
            #     right -=1

            if right > len(nums):
                left +=1
                

    return count

# print(triangleNumber(nums))



# def triangleNumber1(nums) -> int:
#     nums=sorted(nums)
#     count=0
#     for i in range(len(nums)):
#         n=len(nums)
#         left=i+1
#         right=n-1
#         while left<right:
#             if nums[i]+nums[left]>nums[right]:
#                 count +=1
#                 right -=1
#             else:
#                 right -=1
#             if left==right:
#                 left +=1
#                 right=n-1
                

#     return count

# print(triangleNumber1(nums))




