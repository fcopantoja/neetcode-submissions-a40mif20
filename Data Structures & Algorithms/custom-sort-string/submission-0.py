class Solution:
    def customSortStringNaive(self, order: str, s: str) -> str:
        ranking = {c: idx for idx, c in enumerate(order)}

        st = sorted(list(s), key=lambda x: ranking.get(x, 26))
        return ''.join(st)

    def customSortString(self, order: str, s: str) -> str:
        counts = defaultdict(int)
        res = ""

        for ch in s:
            counts[ch] += 1
        
        for ch in order:
            if ch in counts:
                while counts[ch]:
                    res += ch
                    counts[ch] -= 1

        for i in range(26):
            ch = chr(ord('a') + i)
            if counts[ch] > 0:
                while counts[ch]:
                    res += ch
                    counts[ch] -= 1
        
        return res