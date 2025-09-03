arr = [0,-2,2]
answer = False
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] == 2 * arr[j] and i!=j:
            answer = True
print(answer)
    