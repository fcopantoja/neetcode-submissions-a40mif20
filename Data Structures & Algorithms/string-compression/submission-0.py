class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        l = 0
        n = len(chars)
        result = []
        write = 0

        while i < n:
            curr_char = chars[i]
            print(curr_char)
            j = i

            while j < n and chars[i] == chars[j]:
                j += 1

            length = str(j - i)
            chars[write] = curr_char
            write += 1
            #result.append(curr_char)
            if length != "1":
                for ch in length:
                    chars[write] = ch
                    write += 1
            
            i = j
        
        return write