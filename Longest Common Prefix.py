strs = ["flower","flow","flight"]

"""answer = "".join(map(str, set.intersection(*[set(i) for i in strs])))"""

"""for i in range(len(min(strs, key = len))):
    if strs[0][i] in strs:
        """

"""for word in strs:
    for j in range(len(min(strs, key = len))):
        if word in strs[i-1][j]:
            answer += (strs[0][i-1])
            break
    answer += i[0]"""
for i in range(len(strs[0])-1):
    answer = strs[0][i]
    for j in range(1, len(strs)):
        if i == len(strs[j]) or strs[j][i] !=answer:
            print(strs[0][:i])
            break
#print(strs[0])

"""
answer = strs[0]
for i in range(1, len(min(strs, key = len))-1):
    answer = ''.join(set(answer).intersection(strs[i]))
print(answer)
"""