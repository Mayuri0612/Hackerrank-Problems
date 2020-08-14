if __name__ == "__main__":
    stack = []
    n = int(input())
    for i in range(0,n):
        choice = input()
        query = choice[0]
        if query == '1':
            val = int(choice[2:])
            push(stack, val)
        elif query == '2':
            pop(stack)
        else:
            maxEle(stack)