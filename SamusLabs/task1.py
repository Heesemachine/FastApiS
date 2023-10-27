numbers = []
for i in range(1001):
    if i ** 2 <= 1000 or i ** 3 <= 1000:
        numbers.append(i)

def custom_sort_key(number):
    reversed_str = str(number)[::-1]
    return int(reversed_str)

sorted_numbers = sorted(numbers, key=custom_sort_key)

print(sorted_numbers)