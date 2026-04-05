class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        i = 0

        mapping = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000,
        }

        res = 0
        while i < len(s):
            if s[i:i + 2] in ["IX", "IV", "XL", "XC", "CM", "CD"]:
                res += mapping.get(s[i:i + 2], 0)
                i += 2
            else:
                res += mapping.get(s[i], 0)
                i += 1
        
        return res


