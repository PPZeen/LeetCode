class Solution:
    def isValid(self, s: str) -> bool:
        b = {'}':'{', ')':'(', ']':'['}
        a = []
        for c in s:
            if c in '{[(': a.append(c)
            else:
                if len(a) == 0 or a[-1] != b[c]: return False
                a.pop() 
        return not a