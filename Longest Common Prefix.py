strs = ["flower","flow","flight"]

answer = ""
strs = sorted(strs)
print(strs)
first = strs[0]
last = strs[-1]
for i in range(min(len(first),len(last))):
    if (first[i] != last[i]):
        print(answer)
    answer += first[i]
print(answer)
