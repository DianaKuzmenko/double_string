# double_string
def double_str('aa'):
    s1 = '*' + s
    print(s1)
    while len(s1) < (2*len(s)+1):
        s1 = s1.replace('*a','aa*')
        print(s1)
    s1 = s1.replace('*','')
    print(s1)
    print(len(s1))
