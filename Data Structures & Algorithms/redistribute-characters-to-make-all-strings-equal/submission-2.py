class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counts = defaultdict(int)

        for word in words:
            for ch in word:
                counts[ch] += 1
        
        for k, v in counts.items():
            if v % len(words) != 0:
                return False
        
        return True
