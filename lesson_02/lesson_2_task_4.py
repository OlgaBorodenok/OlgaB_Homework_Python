#Напишите функцию fizz_buzz, которая принимает один аргумент — n (число).
# Функция должна печатать числа от 1 до n. При этом:
# если число делится на 3, печатать Fizz;
# если число делится на 5, печатать Buzz;
# если число делится на 3 и на 5, печатать FizzBuzz.

def fizz_buzz(n):
    for num in range(1, n + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

fizz_buzz(15)