def pangrams(s):
    d = s.replace(" ","")
    l1 = []
    res =[]
    for i in range(65,91):
        l1+=chr(i)
    for j in range(97,123):
        l1+=chr(j)
    c = len(d)
    f = chr(c)
    for f in d:
        res += f
    print(res)
    for z in res:
        if z not in l1:
            s ="not pangram"
            return s
        elif z in l1:
            g ="pangram"
    return g
print(pangrams("We promptly judged antique ivory buckles for the next prize"))
            