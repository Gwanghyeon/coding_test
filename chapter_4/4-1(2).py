# Checking time including the number you like
# type of complete search

print("Which number you like to check? ", end=None)
checking_num = input()
n = int(input())

count = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if checking_num in str(i)+str(j)+str(k):
                count += 1


print(count)
