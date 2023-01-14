n=int(input())
result=""
for each in range(n):
    s1,s2=input().split()
    if len(s1)==len(s2):
        s1=list(s1)
        s2=list(s2)
        for j in s1:
            if j in s2:
                s2.remove(j)
            else:
                break
        if len(s2)==0:
            result+="YES "
        else:
            result+="NO "
    else:
        result+="NO "

print(result)
    