def knapsack(w, wt, pro, n):
	k = [[0 for x in range(w+1)]for x in range(n+1)]

	for i in range(n+1):
		for w in range(w+1):
			if i == 0 or w == 0:
				k[i][w] = 0
			elif wt[i-1] <= w:
				k[i][w] = max(pro[i-1]+ k[i-1][w-wt[i-1]], k[i-1][w])
			else:
				k[i][w] = k[i-1][w]
	return k[n][w]

profit = [1, 6, 18, 22, 28]

weight = [1, 2 ,5, 6, 7]

capacity = 11

obj = len(weight)

print("maximum profit is:   "+ str(knapsack(capacity, weight, profit, obj))) 