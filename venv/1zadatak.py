def prvi(a, b, op):
    return{
        '+' : a + b,
        '-' : a - b,
        '*' : a * b

    }.get(op, a + b)

rez = prvi(1 , 2, '+')
rez1 = prvi(2, 3, '-')
rez2 = prvi(4, 5, '*')
rez3 = prvi(1,2,'')

print(rez)
print(rez1)
print(rez2)
print(rez3)