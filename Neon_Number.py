n=int(input())
sum=0
squre=n*n
while squre>0:
    r=squre%10
    sum=sum+r
    squre=squre//10
if (sum == n):
    print('Neon Number')
else:
    print('Not Neon Number')