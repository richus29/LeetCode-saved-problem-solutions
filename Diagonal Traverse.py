mat = [[1,2,3],[4,5,6],[7,8,9]]
diagonals = {}
answer = []
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if i + j not in diagonals:
            diagonals[i+j] = [mat[i][j]]
        else:
            diagonals[i+j].append(mat[i][j])
for item in diagonals.items():
    if item[0] % 2 == 0:
        [answer.append(x) for x in item[1][::-1]]
    else:
        [answer.append(x) for x in item[1]] 
print(answer) 