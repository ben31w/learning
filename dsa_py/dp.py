"""
Dynamic Programming (DP) is an optimization for recursive problems
(problems with overlapping subproblems). Each subproblem is solved once, 
and its result is stored in memory instead of making unnecessary recursive calls.
This usually reduces time complexity from exponential to polynomial.

You must derive a recurrence relation relating subproblems to their previous
smaller subproblems.

ex: F(n) = F(n-1) + F(n-2) for n >1
    F(1) = 1
    F(0) = 0
"""
### Fibonacci sequence ###
# ith number is sum of i-1, i-2
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

def fib_rec(i):  # O (2^N)
    if i <= 1:
        return i
    return fib_rec(i-1) + fib_rec(i-2)


def _fib_dp(i, dp):
        # print(f"fib(i={i}, dp={dp})")
        if i <= 1:
            return i
        
        if dp[i] != -1:  # check if result is already in table
            return dp[i]
        
        dp[i] = _fib_dp(i - 1, dp) + _fib_dp(i - 2, dp)
        # print(f"fib(i={i}, dp={dp}) -> {dp[i]}")
        return dp[i]

def fib_dp(i):  # O(N)
    dp = [-1] * (i + 1)
    return _fib_dp(i, dp)


### Coin Row ###
# - Row of n coins expressed as positive ints [c1, c2, ..., cn]
# - Get mox amount of money from row, but no adjacent coins can be collected.