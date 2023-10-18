class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans = ''
        lenght = len(strs) - 1
        for i in range(min(map(len, strs))):
            for s in range(lenght):
                if strs[s][i] != strs[s+1][i]: return ans
            ans += strs[0][i]

        return ans