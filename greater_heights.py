def greater_heights(q_list,h):
    for q in q_list:
        count=0
        for i in h:
            if i>=q:
                count+=1
        print(count)        

N,Q=list(map(int,input().split()))
h=list(map(int,input().split()))
q_list=[]
for i in range(Q):
    x=int(input())
    q_list.append(x)
greater_heights(q_list,h)
    