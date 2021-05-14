# Pibonazzi

# Simple recursive function
def pibo_simple(x):
    if x == 0 or x == 1:
        return 1
    return pibo(x-1)+pibo(x-2)


array = [0]*100
array[0] = 1
array[1] = 1


def pibo_memo(x):
    if array[x] != 0:
        return array[x]

    else:
        array[x] = pibo_memo(x-1)+pibo_memo(x-2)

    return array[x]


print(pibo_memo(5))
print(array)


def pibo_bottom_up(x):
    for i in range(3, 100):
        array[i] = array[i-1]+array[i-2]


pibo_bottom_up(20)

print(array)
