def postfix(expression):
    stack=[]
    for i in expression :
        if i.isdigit()  :
            stack.append(int(i))
        else:
            if len(stack)>2:
                exp1=stack.pop()
                exp2=stack.pop()
                if i =='+':
                    stack.append(exp2 + exp1)
                elif i =='-':
                    stack.append(exp2 - exp1)
                elif i =='*':
                    stack.append(exp2 * exp1)
                elif i =='/':
                    stack.append(exp2 / exp1)
        print(stack)
    for i in range(len(stack)-1):
        exp1 = stack.pop()
        print(exp1,end=' ')
a='5*(6+2)-12/4'
postfix(a)

