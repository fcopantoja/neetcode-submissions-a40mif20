class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        a = 0
        for num in num1:
            digit = ord(num) - ord('0')
            a = (a * 10) + digit

        b = 0
        for num in num2:
            digit = ord(num) - ord('0')
            b = (b * 10) + digit
            

        return str(a * b)
        print(a, b)
