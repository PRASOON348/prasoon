import string

def mutate_string(string,i,c):
    l = list(string)
    l[i] = c
    string = "".join(l)
    return string

s = mutate_string(" thop", 0,"sunny")
print(s)
