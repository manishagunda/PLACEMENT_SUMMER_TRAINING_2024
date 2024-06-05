def sum_even_in_a_odd_in_b(a, b):
    sum_even_a = sum(num for num in a if num % 2 == 0)
    sum_odd_b = sum(num for num in b if num % 2 != 0)
    return [sum_even_a, sum_odd_b]
a = [3, 8, 5, 4, 3]
b = [5, 0, 9, 3, 2]
result = sum_even_in_a_odd_in_b(a, b)
print(result)