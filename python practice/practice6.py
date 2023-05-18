def add_minus(x, y):
    a = x + y
    if(x < y):
        b = y - x
    else:
        b = x - y
    return a, b
    
while True:
    c = input('첫 번째 숫자를 입력하세요:')
    d = input('두 번째 숫자를 입력하세요:')
    if c == '' or d == '':
        break
    else:
        f,s = add_minus(int(c),int(d))
        print('합:',f,' 차:',s)