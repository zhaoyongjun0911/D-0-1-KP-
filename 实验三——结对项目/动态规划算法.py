def pack(w, v, n, c):
	dp = [0 for _ in range(c+1)]
	for i in range(1, len(w)+1):
	    for j in reversed(range(1, c+1)):
	        for k in range(3):
	            if j-w[i-1][k] >= 0:
	                # print(dp[j])
	                dp[j] = max(dp[j], dp[j-w[i-1][k]] + v[i-1][k])
	    # print(dp)
	print(dp[c])