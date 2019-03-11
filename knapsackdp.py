def knapsack(wt,val,W,n):
    T=[[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(n+1):
        for j in range(W+1):
            if i==0 or j==0:
                T[i][j]=0
            elif wt[i-1]>j:
                T[i][j]=T[i-1][j]
            else:
                T[i][j]=max(T[i-1][j],val[i-1]+T[i-1][j-wt[i-1]])
    print 'maximum value : ', T[n][W]
    res=T[n][W]
    w=W
    print 'weights : '
    for i in range(n,0,-1):
        if res<=0:
            break
        if res==T[i-1][w]:
            continue
        else:
            print wt[i-1]
            res=res-val[i-1]
            w=w-wt[i-1]

def main():
    #wt=[1,3,4,5]
    #val=[1,4,5,7]
    wt=[]
    val=[]
    with open('knapsackdpinpwt.txt','r') as myfile:
        for line in myfile:
            wt.extend(map(int,line.split(',')))
    with open('knapsackdpinpval.txt','r') as myfile:
        for line in myfile:
            val.extend(map(int,line.split(',')))
    print 'weights : ', wt
    print 'values : ', val
    W=15;
    print 'capacity of knapsack : ', W
    n=len(val)
    print '\n'
    knapsack(wt,val,W,n)
main()
