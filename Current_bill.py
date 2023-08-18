units=int(input())
uc=0
bill=0
sr=0
tb=0
if units<200:
    bill=units*1.20
elif(units>=200 and units<400):
    bill=units*1.50
elif(units>=400 and units<600):
    bill=units*1.80
else:
    bill=units*2.00
if(bill>=400):
    sr=bill*0.15
    tb=bill+sr
    print("%.2f"%tb)
else:
    tb=bill+100
    print("%.2f"%tb)