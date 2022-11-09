

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        string = str(x)

        half = len(string) / 2
        if isinstance(x, float):
            half += 1
    
        
        for i in range(int(half)):
            if string[i] != string[-(i+1)]:
                return False
            
        return True
