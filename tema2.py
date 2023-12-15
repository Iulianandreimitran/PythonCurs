
print("Exercitiul 1:")

def sum_numbers(*args, **kwargs):
    total = 0
    for arg in args:
        if type(arg) is int or type(arg) is float:
            total +=arg
    return total

print(sum_numbers(1, 5, -3, 'abc', [12, 56, 'cad']))
print(sum_numbers())
print(sum_numbers(2, 4, 'abc', param_1=2))


print("Exercitiul 2:")
def sum_recursive(numbers):
    if not numbers:
        return 0, 0, 0

    number = numbers[0]
    sum_total, sum_even, sum_odd = sum_recursive(numbers[1:])

    sum_total += number
    if number % 2 == 0:
        sum_even += number
    else:
        sum_odd += number

    return sum_total, sum_even, sum_odd

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
total_sum, even_sum, odd_sum = sum_recursive(numbers_list)
print(f"Suma totală: {total_sum}")
print(f"Suma numerelor pare: {even_sum}")
print(f"Suma numerelor impare: {odd_sum}")


print("Exercitiul 3:")

def read_number():
    number_keyboard = input("Introduceti un numar intreg: ")
    if number_keyboard.isdigit():
        return number_keyboard
    else:
        print("Numarul introdus nu este intreg ")
        return 0

number = read_number()
print(f"Rezultatul: {number}")


