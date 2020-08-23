#reversing an integer
class Solution:
    def reverse(self, x: int) -> int:
        maxi = (pow(2,31) - 1)
        mini = pow(-2,31)
        
        rev = 0
        if x > 0:
            while(x > 0):
                dig = x % 10
                rev = rev * 10 + dig
                x = x//10
            if rev > maxi or rev < mini:
                return 0
            return rev
        
        if x == 0:
            return 0
        
        if x < 0:
            x =abs(x)
            while(x > 0):
                dig = x % 10
                rev = rev * 10 + dig
                x = x//10
            if rev > maxi or rev < mini:
                return 0
            return (-rev)