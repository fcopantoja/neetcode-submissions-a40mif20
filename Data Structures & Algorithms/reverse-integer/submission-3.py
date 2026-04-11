
class Solution:
    def reverse(self, x: int) -> int:
        y = abs(x)
        res = 0
        while y:
            digit = y % 10
            res = res * 10 + digit
            y = y // 10
        
        print(res)
        if not res:
            return 0
        
        res = res if x > 0 else -res
        if res > (2 ** 31) or res < (-2 ** 31):
            return 0
        
        return res