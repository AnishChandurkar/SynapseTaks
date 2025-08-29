def lumos(runes):
    has_L = has_U = has_M = has_O = has_S = 0
    
    for i in range(len(runes)):
        r = runes[i]
        step = i + 1
        ch = r.upper()
        
        if ch == 'L':
            has_L = 1
        elif ch == 'U':
            has_U = 1
        elif ch == 'M':
            has_M = 1
        elif ch == 'O':
            has_O = 1
        elif ch == 'S':
            has_S = 1
        
        if has_L and has_U and has_M and has_O and has_S:
            return step
    
    return -1

runes = input("Enter runes ")
print(lumos(runes))