a = float(input("Enter the a with they're +- "))
b = float(input("Enter the b with they're +-"))
c = float(input("Enter the c with they're +- "))

if a == 0:
    print("A cannot be zero")
elif b > 0:
    print(f'{a}x^2 + {b}x + {c}')
elif b < 0:
    print(f'{a}x^2 -{b}x  + {c}')
elif b == 0:
    print(f'{a}x^2 + {c}')
elif c < 0:
    print(f'{a}x^2 -{b}x  - {c}')
elif c > 0:
    print(f'{a}x^2 -{b}x  + {c}')
elif c == 0:
    print(f'a{a}x^2 + {b}x')

d = input("Do you want the discriminant value or the x1,x2 ?:")
awns = b * b - 4 * a * c

if d.lower() == "d":
    print(awns)
elif d.lower() == "x":
    x1_x2 = (-(b) + awns**(1/2))/2*a
    print(f'x1 = {x1_x2}')
    x3_x4 = (-(b) - awns**(1/2))/2*a
    print(f'x2 = {x3_x4}')
