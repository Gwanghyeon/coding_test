#recurrence relation 
#a[i]=max(a[i-1] or a[i-2]+k[i]) 
#a[i] // i번째까지의 최대합


array=list(map(int, input().split()))

d=[0]*10000
d[0]=array[0]
d[1]=max(array[0],array[1])

for i in range(2, len(array)+1):
    d[i]=max(d[i-1], d[i-2]+array[i])
