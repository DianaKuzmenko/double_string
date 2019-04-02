def double_str('aa'):
    s1 = '*' + s
    while len(s1) < (2*len(s)+1):
        s1 = s1.replace('*a','aa*')
    s1 = s1.replace('*','')
    print(s1)
