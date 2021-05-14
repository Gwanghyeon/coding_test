# slicing rice cakes

n = int(input())
array = list(map(int, input().split()))

start, result = 0
end = max(array)

while start <= end:
    total = 0
    mid = (start+end)//2
    for x in array:
        total += x-mid
    if total < n:
        end = mid-1
    else:
        result = mid
        start = mid+1

print(result)


#practice
object=int(input())

array=list(map(int, input().split()))

end=max(array)
start, result=0

while start<=end:
    total=0
    mid=(start+end)//2

    for x in array:
        if x>mid:
            total+=(x-mid)
    
    if total<object:
        end=mid-1
    else:
        result=mid
        start=mid+1

#need to graphicalize the process, workig on that tomorrow!


