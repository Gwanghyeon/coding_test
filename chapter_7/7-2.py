#부품찾기

#binary search
def binary_search(array, target, start, end):
    while start<=end:
        mid=(start+end)//2
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None

array=list(map(int, input().split()))
target_array=list(map(int, input().split()))

array.sort()

for target in target_array:
    if binary_search(array, target, 0, (len(array)-1))!=None:
        print("yes")
    else:
        print("no")


#using set
array=set(map(int, input().split()))

for target in target_array:
    if target in array:
        print("yes")
    else:
        print("no")