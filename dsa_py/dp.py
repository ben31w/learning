"""
Dynamic Programming (memo) is an optimization for recursive problems
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

def fib_rec(i):
    """Terrible recursive approach. O(2^N)"""
    if i <= 1:
        return i
    return fib_rec(i-1) + fib_rec(i-2)


def _fib_memo(i, memo):
    # print(f"fib(i={i}, memo={memo})")
    if i <= 1:
        return i
    
    if memo[i] != -1:  # check if result is already in table
        return memo[i]
    
    memo[i] = _fib_memo(i - 1, memo) + _fib_memo(i - 2, memo)
    # print(f"fib(i={i}, memo={memo}) -> {memo[i]}")
    return memo[i]

def fib_memo(i):
    """
    Dynamic programming memoization (top-down) builds a table starting 
    at top, making recursive calls that shrink the problem. O(N)
    """
    memo = [-1] * (i + 1)
    return _fib_memo(i, memo)

def fib_tab(n):
    """
    Dynamic programming tabulation (bottom-up) builds a table starting
    from bottom, using a loop to calculate fill in the table using previous
    table values. O(N)
    """
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i -2]
    
    return dp[n]

def fib(n):
    if n <= 1:
        return n

    prev_prev, prev, curr = 0, 1, 1

    for i in range(2, n + 1):
        curr = prev + prev_prev
        prev_prev = prev
        prev = curr
    
    return curr


print(fib(5))


### Coin Row ###
# - Row of n coins expressed as positive ints [c1, c2, ..., cn]
# - Get mox amount of money from row, but no adjacent coins can be collected.