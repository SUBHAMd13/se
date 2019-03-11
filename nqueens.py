n=input("enter no.of queens : ")
board=[0]*(n+1)
print(board)
count=1

def printboard():
    global count
    print('solution '), count
    count=count+1
    for i in range(1,n+1):
        print("\t"),i,
    print ("\n")
    for i in range(1,n+1):
        print i,
        for j in range(1,n+1):
            if (board[i]==j):
                print("\tQ"),
            else:
                print("\t-"),
        print("\n")

def place(row,col):
    for i in range(1,row):
        if(board[i]==col):
            return 0
        elif (abs(board[i]-col)==abs(i-row)):
            return 0
    return 1

def queens(row,n):
    for col in range(1,n+1):
        if(place(row,col)):
            board[row]=col
            if row==n:
                printboard()
            else:
                queens(row+1,n)


def main():
    queens(1,n)
    #print "total solutions : " , count-1
main()
