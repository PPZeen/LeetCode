class Solution:
    def myAtoi(self, s: str) -> int:
        f = 0
        sign = False
        for e in s.strip():
            if e in '0123456789': f += 1
            else:
                if e in '-+':
                    if sign:
                        if f > 1: break
                        return 0
                    elif f > 0: break
                    f += 1
                    sign = True
                    continue
                break

        ans = 0 if f == 0 or (f == 1 and sign) else int(s.strip()[:f:])
        return -2**31 if ans < -2**31 else 2**31-1 if ans > 2**31-1 else ans