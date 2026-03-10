pay=float(input("cena "))
isvip=input('vip li si? ')
fdlvr=input("iskash li expresna? ")
wknd=input("weekend li e? ")
endsum=pay
dlvr=0


if wknd=='da' and fdlvr == 'da':
    dlvr+=3

if pay<100:
    dlvr+=5
    if isvip=='da':
     dlvr-=3

endsum+=dlvr
print('del = ',dlvr)
print('endsum = ', endsum ,' eu')
