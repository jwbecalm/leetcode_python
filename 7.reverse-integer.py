#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.40%)
# Likes:    2281
# Dislikes: 3500
# Total Accepted:    738.4K
# Total Submissions: 2.9M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# 
# Input: 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: 120
# Output: 21
# 
# 
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 0 when the reversed
# integer overflows.
# 
#
class Solution:
    def reverse(self, x: int) -> int:
        # overflow judgement, not here. may overflow after reverse
        if x == 0:
            return 0     

        # convert int to str and list
        res  = list(str(x))
        
        # reverse the list
        res.reverse()

        # if 0 at the index[0]: 120 --> 012 --> 12
        if res[0] == '0':
            res.pop(0)

        # if negtive numer:  -123 --> 321- -->-321
        if res[-1] == '-':
            # inserts '-' at the front of the list
            res.insert(0, '-')
            # remove the last element '-' 
            res.pop()
        
        resint = int(''.join(res))
        # after reverse, do overflow judgement, not at the entry of the function
        if resint <= -2**31 or resint >= 2**31 -1:
            return 0
        else:
            return resint
