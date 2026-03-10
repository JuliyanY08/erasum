gndr=input('muj ili jena? ')
age=int(input('godini? '))
wght=float(input('kila v kg? '))
hght=int(input('visochina v sm? '))
act=int(input('akt ot 1-3 ? '))
cals=int(input('prieti cals? '))

if gndr=='muj':
    BMR=10*wght+6.25*hght-5*age+5
else :
    BMR=10*wght+6.25*hght-5*age-161

if act==1:
    act=1.2
elif act==2:
    act=1.55
elif act==3:
    act=1.9

BMR*=act
print('prepor = ',BMR)
if cals<BMR:
    print('priel po malko s ', (BMR-cals))
else:
    print('priel poveche s ', (cals-BMR))