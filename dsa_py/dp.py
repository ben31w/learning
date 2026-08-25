"""
Dynamic Programming (DP) is an optimiation for recursive problems.
It stores the result in memory instead of making redundant recursive calls.
This usually reduces time complexity from exponential to polynomial.
"""

# Fibonacci sequence
# ith number is sum of i-1, i-2
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

def fib_rec(i):  # O (2^N)
    if i <= 1:
        return i
    return fib_rec(i-1) + fib_rec(i-2)

def fib_dp(i):
    dp = [-1] * (i + 1)

    def fib(i, dp):
        if i <= 1:
            return i

        # check if result is already in table
        if dp[i] != -1:
            return dp[i]
        
        dp[i] = fib(i - 1, dp) + fib(i - 2, dp)
        return dp[i]

    return fib(i, dp)


for i in range(10):
    print(fib_dp(i))
