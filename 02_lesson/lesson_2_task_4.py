n = int(input("Введите число: "))

def fizz_buzz(n):
    for a in range(1, n + 1):
        if a % 3 == 0:
            print("Fizz")
        elif a % 5 == 0:
            print("Buzz")
        elif a % 3 == 0 and a % 5 == 0:
            print("FizzBuzz")
        else:
            print(a)

fizz_buzz(n)