def check():
    n = int(input())
    inputs = []
    answers = ['YES'] * n 

    for _ in range(n):
        inputs.append(input()) 

    for i in range(n):
        stack = [];
        for j in range(len(inputs[i])): 
            if (inputs[i][j] == '(') : stack.append(j)
            elif ( inputs[i][j] == ')') :
                if len(stack) == 0 : 
                    answers[i] = 'NO'
                    break;
                else:  stack.pop()
        if len(stack) : 
            answers[i] = 'NO' 
    
    print("\n".join(answers))
check();