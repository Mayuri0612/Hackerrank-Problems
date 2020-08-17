def longestparen(string):
    count = 0
    ret = 0
    stk = []
    for j in range(0,len(string)):
        if(string[j] == '('):
            stk.append(count)
            count = 0
        elif(len(stk) > 0 and string[j] == ')'):
            count += stk.pop() + 2
            ret = max(count, ret)

        elif(len(stk) > 0 and string[j] == ')'):
            count = 0
    return ret


t = int(input())
for i in range(t):
    string = str(input().split())
    print(longestparen(string))
    '''
    string = str(input().split())
    for j in range(0,len(string)):
        #sum = 0
        if(string[j] == '(' and string[j+1] == ')'):
            sum = sum + 2
            '''
    