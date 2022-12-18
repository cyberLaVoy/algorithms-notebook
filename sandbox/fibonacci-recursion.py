
def fib(position, initial=True, numbers={}): 
    negative = False
    if initial and position%2 == 0 and position < 0:
        negative = True
    if position < 0:
        position = 0 - position
    if position == 0:
        return 0
    if position <= 2 and position > 0:
        return 1
    if position in numbers:
        number = numbers[position]
        if negative:
            number = 0 - number
        return number
    number = fib(position - 1, False, numbers) + fib(position - 2, False, numbers)
    numbers[position] = number
    if negative:
        number = 0 - number
    return number

def main():
    while True: 
        position = input("Fibonacci #")
        position = int(position)
        number = fib(position)
        print(number)
main()
