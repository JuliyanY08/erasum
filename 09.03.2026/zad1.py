bra=int(input("qbalki "))

brb=int(input("banani "))
brs=int(input("sandvichi "))
brp=int(input("pica "))

brac=bra*52
print(brac)
brbc=brb*89
print(brbc)
brsc=brs*250
print(brsc)
brpc=brp*285
print(brpc)

totcal=brac+brbc+brsc+brpc

print("totcal " ,totcal)

if totcal<=2000:
    print('gj')
else:
    print('bj')