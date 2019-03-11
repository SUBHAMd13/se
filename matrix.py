import sys

def matrix_mult(p, n):
	m = [[0 for x in range(n)] for x in range(n)]
	
	for i in range(1,n):
		m[i][i] = 0
	for L in range(2,n):	
		for i in range (1, n-L+1):
			j = i+L-1
			m[i][j] = sys.maxint
			for k in range(i,j):
				q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
				if(q < m[i][j]):
					m[i][j] = q
	return m[1][n-1]

fil1 = open("xyz.txt","r")
stri = fil1.read()
arr = []

for val in stri.split():
	arr.append(int(val))

size = len(arr)

fil2 = open("out.txt","w")
fil2.write(str(matrix_mult(arr, size)))
fil1.close()
fil2.close()