def denom(amount):
    #coin=[2000,500,200,100,50,20,10,5,2,1]
    coin=[]
    with open('input1.txt','r') as myfile:
        for line in myfile:
            coin.extend(map(int, line.split(',')))
    coin.sort(reverse=True)
    for i in range(0,len(coin)):
        print coin[i]
    file=open('output.txt','w')
    for i in range(0,len(coin)):
        if amount>=coin[i]:
            j=amount/coin[i]
            amount=amount-j*coin[i]
            #print coin[i] ,":", j
            #file=open('output.txt','w')
            file.write("%s : " % coin[i]);
            file.write("%s\n" % j);
    
    file.close();
    
    if amount!=0:
        print "remaining amount : " , amount

def main():
    amount=input("enter the amount : ")
    denom(amount)
main()