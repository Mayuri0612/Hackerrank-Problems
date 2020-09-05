#Given 2 integers m, and n (decimal system), 
#write a program to perform right shift on m , n times.
def rightShift(m,n):
    return (m >> n)

n, m = map(int, input().split())
print( rightShift(m,n) )


