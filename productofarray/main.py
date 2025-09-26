# Product of array without self 
arr=[1,2,3,4]

#bf
# complexity O(n^2)
values=[]
for i in range(len(arr)):
    product=1
    for num in arr[:i]+arr[i+1:]:
        product *=num
    values.append(product)
# print(values)

#optimal
post=1
pre=1
ans=[1]*len(arr)
for i in range(len(arr)):
    ans[i]=pre
    pre=pre*arr[i]
    
print(ans)
for i in range(len(arr)-1,-1,-1):
    ans[i]=ans[i]*post
    post= post* arr[i]
       
print(ans)
    
