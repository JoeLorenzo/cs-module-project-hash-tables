import math

# Inverse square root is 1 / square root of number
# Relatively time consuming
def get_inverse_square(num):
    return 1 / math.sqrt(num)



# We need to constantly get the inverse square roots of numbers between 1 and 1000

# what should our lookup table look like? 
# Keys will be numbers
# Values will be results of get_inverse_square


def build_lookup_table():
    lookup_table = {}
    for i in range(1, 1001):
        lookup_table[i] = get_inverse_square(i)
    return lookup_table


sqrt_lookup_table = build_lookup_table()

print(sqrt_lookup_table[3])
print(sqrt_lookup_table[982])
print(sqrt_lookup_table[234])
