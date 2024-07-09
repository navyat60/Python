def half_adder(a, b):
    sum_result = a ^ b
    carry = a & b
    return sum_result, carry
a = 1   
b = 0
sum_result, carry = half_adder(a, b)

print("Inputs: a =", a, "b =", b)
print("Sum:", sum_result)
print("Carry:", carry)
