def double_str(s):
    s1 = '*' + s
    result=s1
    while len(s1) < (2*len(s)+1):
        s1 = s1.replace('*a','aa*')
        result +=s1
    s1 = s1.replace('*','')
    print(result)
