#valid anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        x = sorted(s)
        y = sorted(t)
        
        if len(x) != len(y):
            return False
        
        if len(x) == 0 or len(y) == 0:
            return True
        
        i = 0
        while(i <= len(x)-1):
            if x[i] != y[i]:
                return False
                break
                
            if x[i] == y[i]:
                i += 1
        return True
    