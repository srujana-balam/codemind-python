import math
p=int(input())
r=float(input())
t=int(input())
ci=p*pow((1+r/100),t)-p
print("%.2f"%ci)