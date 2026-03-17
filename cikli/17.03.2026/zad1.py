nums = [3,1,4,1,5,9,2,6,5,3,5]
unq=[]
for num in nums:
    if num not in unq:
        unq.append(num)

print(unq)