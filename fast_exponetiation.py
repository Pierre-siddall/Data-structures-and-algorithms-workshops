def binarymultiplecount(exponent):
    count = 0
    binary_rep = bin(exponent)
    while exponent != 0:
        exponent = exponent//2
        count += 1
    for item in binary_rep:
        if item == '1':
            count += 1
    return count-2


def binaryexponetiation(x, exponent):
    binary_rep = bin(exponent)
    binary_rep = binary_rep[2:]
    result = 1
    binary_weights = [2**y for y in range(len(binary_rep))]
    binary_weights.reverse()
    for bit in range(len(binary_rep)):
        if binary_rep[bit] == '1':
            result *= x**binary_weights[bit]
        else:
            pass
    return result
