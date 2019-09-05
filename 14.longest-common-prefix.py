#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (34.06%)
# Likes:    1583
# Dislikes: 1446
# Total Accepted:    532.3K
# Total Submissions: 1.6M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# Example 1:
# 
# 
# Input: ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# 
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# Note:
# 
# All given inputs are in lowercase letters a-z.
# 
#
class Solution:
    def getNewCommonPrefix(self, oldStr: str, newStr:str) ->str:
        if (len(oldStr) == 0 or len(newStr) == 0):
            return ''
        # if the first char is different, return ''
        if oldStr[0] != newStr[0]: 
            return ''

        res = ''
        minLen = min(len(oldStr), len(newStr))        
        for i in range(minLen):
            if oldStr[i] == newStr[i]:
                res += oldStr[i]
        return res
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # check whether list is empty
        if len(strs) == 0:
            return ''

        # set commonPreifx = list[0]
        commonPrefix = strs[0]
        # iterator the rest of list
        for i in range(1, len(strs)):
            # compare and get the new common prefix
            commonPrefix = self.getNewCommonPrefix(commonPrefix,strs[i] )
        return commonPrefix
