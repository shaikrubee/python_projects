def sum_of_range(m,n,s):
    sum=0
    for each in s:
        if(m<=each<=n):
            sum+=each
    return sum        

s=list(map(int,input().split()))
m=int(input())
for i in range(m):
    m,n=map(int,input().split())
    result=sum_of_range(m,n,s)
    print(result)