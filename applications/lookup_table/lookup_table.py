import random
import math

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653
    return v

    

powers = {}
factorials = {}
divisibles = {}
modulos = {}

# populate the powers dictionary given a range
for x in range(2, 14):
    for y in range(3, 6):
        powers[f"{x},{y}"] = int(math.pow(x, y))

# populate the factorials dictionary given all possible powers 
for key, value in powers.items():
    factorials[value] = math.factorial(value)
 
# populate the divisible dictionary given all possible factorial 
for key, value in factorials.items():
    divisibles[value] = value // (x + y)

# populate the modulos dictionary given all possible divisibles 
for key, value in divisibles.items():
    modulos[value] = value % 982451653

# print(powers)
# print(factorials)
# print(divisibles)
# print(modulos)


def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    v = powers[f"{x},{y}"]
    v = factorials[v]
    v = divisibles[v]
    v = modulos[v]
    return v

# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
