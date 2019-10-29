#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ret = []
        if not digits or not len(digits):
            return ret
        self.dfs(digits, 0, "", ret)
        return ret
    
    def dfs(self, digits, level, out, ret):
        if len(out) == len(digits):
            ret.append(out[:])
            return
        kvmaps = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', \
             '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        for i in kvmaps[digits[level]]:
            self.dfs(digits, level + 1, out + i , ret)
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits or not len(digits):
            return
        
        kvmap = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', \
             '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
        def _dfs(digits, ret, level, out, kvmap):
            if len(out) == len(digits):
                ret.append(out)
                return
            for c in kvmap[digits[level]]:
                _dfs(digits, ret, level + 1, out + c, kvmap)
        
        ret = []
        _dfs(digits, ret, 0, "", kvmap)
            
        return ret
'''
# @lc code=end

