import re
def decodeString(s):
    stack = []
        
    for x in s:
        if x != ']':
            stack.append(x)
        else:
            t = []
            while stack and stack[-1] != '[':
                t.append(stack.pop())
            stack.pop()
            l = ''
            while stack and stack[-1].isdigit():
                l = l+stack.pop()
            l = int(l[::-1])
            stack.append((''.join(t[::-1]))*int(l))

    return ''.join(stack)
            
    

decodeString("3[a2[c]]")