#Monk and suffix sort
s, k = input().split()
K = int(k)
new = []
n = len(s)
for i in range(n):
    new.append(s[i:n])
new.sort()
print(new[K-1])
    
