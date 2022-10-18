def handler(operator: str, stack: list, x: str):
    if operator == '.':
        #print(stack)
        #print(stack[len(stack) - 2], '.', stack[len(stack) - 1])
        item = stack.pop()
        stack[len(stack) - 1] += item

    elif operator == '+':
        #print(stack)
        #print(stack[len(stack) - 2], '+', stack[len(stack) - 1])
        if len(stack[len(stack) - 1]) == 0:
            stack.pop()
        elif len(stack[len(stack) - 2]) == 0:
            stack.pop(len(stack) - 2)
        elif (stack[len(stack) - 1] == len(stack[len(stack) - 1]) * x) \
                or (stack[len(stack) - 1][0] == x and stack[len(stack) - 2][0] != x):
            stack.pop(len(stack) - 2)
        elif stack[len(stack) - 1][0] == x and stack[len(stack) - 2][0] == x:
            c1 = c2 = 0
            ct1 = ct2 = True
            for i in range(max(len(stack[len(stack) - 1]), len(stack[len(stack) - 2]))):
                try:
                    el1 = stack[len(stack) - 1][i]
                    if el1 == x and ct1 != False:
                        c1 += 1
                    else:
                        ct1 = False
                except:
                    pass
                try:
                    el2 = stack[len(stack) - 2][i]
                    if el2 == x and ct2 != False:
                        c2 += 1
                    else:
                        ct2 = False
                except:
                    pass
            stack.pop() if c2 >= c1 else stack.pop(len(stack) - 2)
        else:
            stack.pop()

    elif operator == '*':
        #print(stack)
        #print(stack[len(stack) - 1], '*')
        if stack[len(stack) - 1] == x or stack[len(stack) - 1] == len(stack[len(stack) - 1]) * x:
            stack[len(stack) - 1] += '*'
        elif stack[len(stack) - 1][0] == x:
            stack[len(stack) - 1] += '*'
        else:
            stack[len(stack) - 1] = ''

    else:
        raise AttributeError("Unexpected command " + operator + "!")

    return stack



def task(alpha: str, x: str):
    # alpha is a regular word in poland form
    # abc++ = a + b + c, ab+* = (a + b)*, ac.b+* = (ac + b)*, a(c + b) = acb+., c + ab^* = cab*.+, (abc) = abc..*
    # ((a + b)(b + c) + (ac)*)c = ab+bc+.ac.*+c.,
    # ((a + b)c + a(ba)*(b + ac))* = ab+c.aba.*.bac.+.+*
    # acb..bab.c.*.ab.ba.+.+*a. = (acb + b(abc)*(ab + ba))*a
    stack = []
    for char in alpha:
        if char != ' ' and char != '.' and char != '+' and char != '*' and (char.isalpha() or char == '1'):
            if char == '1':
                stack.append('')
            else:
                stack.append(char)
        elif char != ' ':
            stack = handler(char, stack, x)

    counter_status = True
    counter = 0
    for i in stack[0]:
        if i == x and counter_status is True:
            counter += 1
        elif i == '*' and counter_status is True:
            counter = "INF"
            break
        else:
            counter_status = False
            break
    return counter