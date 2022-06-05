def print_formatted(n):
    l = len(bin(n)[2:])
    for i in range(1,n+1):
       a = oct(i)[2:]
       b = hex(i)[2:].upper()
       c = bin(i)[2:]
       print(str(i).rjust(l),a.rjust(l),b.rjust(l),c.rjust(l))
print_formatted(17)
