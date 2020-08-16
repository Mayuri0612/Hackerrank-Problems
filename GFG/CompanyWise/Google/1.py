#subarray with given sum

def subarraySum(n,s):
    curr = 0
    Map = {}
    
    for i in range(n):
        curr += arr[i]
        if(curr == s):
            print(1,i+1)
            return 
        elif((curr - s) in Map):
            print(Map[curr-s] + 2,i+1)
            return
        else:
            Map[curr] = i
    print('-1')
    return 
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n,s = map(int, input().split())
        arr = [int(i) for i in input().split()][:n]
        subarraySum(n,s)