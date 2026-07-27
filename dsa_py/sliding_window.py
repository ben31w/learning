"""
Sliding Window is a mental model for solving certain Leetcode problems.
Sliding Window finds a window (subarray) of an array/string/linked list/sequential structure.
Window could be a min, max, longest, shortest, etc.

Sliding Window is O(N). It finds the optimal window by looping over all elements once.

There are several variants of sliding window problems:
- fixed size
- dynamic size: defines a windowStart/left and windowEnd/right. Loop increments windowEnd.
    When a potential solution is found, windowStart is incremented.
- dynamic size with auxiliary data structure (hash map, set)
- string permutations

https://www.youtube.com/watch?v=MK-NZ4hN7rs 
"""
import sys

def maxSumSubarray(nums: list[int], k: int) -> int:
    """
    Fixed size example.
    Given list of nums and subarray size k, find subarray with max total.
    """
    curr_win_sum = 0
    max_win_sum = -sys.maxsize - 1

    for i in range(len(nums)):
        curr_win_sum += nums[i]
        if i >= k:
            curr_win_sum -= nums[i - k]

        max_win_sum = max(max_win_sum, curr_win_sum)
    return max_win_sum


def smallestSubarrayGivenSum(nums: list[int], target_sum: int) -> int:
    """
    Dynamic size example.
    Given list of nums and sum, find smallest subarray size that meets given sum.

    nums = [1,2,3,4]
            0 1 2 3
    target_sum = 7

    curr_win_sum = 4
    min_win_size = 2
    win_start = 3
    win_end = 3
    """
    curr_win_sum = 0
    min_win_size = sys.maxsize
    win_start = 0

    for win_end in range(len(nums)):  # window end is inclusive
        curr_win_sum += nums[win_end]
        while curr_win_sum >= target_sum:
            min_win_size = min(min_win_size, win_end - win_start + 1)

            if min_win_size == 1:
                return 1

            curr_win_sum -= nums[win_start]
            win_start += 1

    return min_win_size

def longestSubstringLenWithKDistinctChars(s: str, k: int) -> int:
    """
    Dynamic size with aux data structure example.
    Given string and number of chars k, find longest substring with k distinct characters.
    """
    max_len = -sys.maxsize - 1
    win_start = 0
    char_map = {}  # char -> count for current window

    for win_end in range(len(s)):
        try:
            char_map[s[win_end]] += 1
        except KeyError:
            char_map[s[win_end]] = 1

        while len(char_map.keys()) > k:
            char_map[s[win_start]] -= 1
            if char_map[s[win_start]] == 0:
                del char_map[s[win_start]]
            win_start += 1

        max_len = max(max_len, win_end - win_start + 1)
    
    return max_len


if __name__ == '__main__':
    print(maxSumSubarray([1,2,3,4,3,2,1], 3))  # -> 3+4+3 -> 10

    print(smallestSubarrayGivenSum([1,2,3,4,3,2,1], 7))  # len([3,4]) -> 2

    print(longestSubstringLenWithKDistinctChars("AAAHHIBG", 2))