nums = [1,2,3,4,5,6,7,8,9,10]
nuums={0:[], 1:[], 2:[]}

for el in nums:
    o = el % 3
    nuums[o].append(el)

print(nuums)
