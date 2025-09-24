arr = [1,2,5,3,2]

# bf solution
# for each element in list check whether similar element available via looping 
# time complexity is O(n^2)
# samape complexity is O(n)
def duplicate_bf(arr):
    for i,num in enumerate(arr):
        if num in arr[i+1:]:
            return True
    return False

print(duplicate_bf(arr))

# optimal solution is using a hash map

def duplicate_optimal(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        else:
            seen.add(num)
    return False

print(duplicate_optimal(arr))

def dup_opti_2(arr):
    without_dup = set(arr)
    if len(arr)>len(without_dup):
        return True
    return False

print(dup_opti_2(arr))
