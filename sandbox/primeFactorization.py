from math import sqrt
def isPrime(value):
    maximum = sqrt(value)
    is_prime = True
    if value > 3:
        if value % 2 == 0:
            return False
        i = 3
        while i <= maximum:
            if value % i == 0:
                is_prime = False
                break
            i += 2
    return is_prime

def divisors(value):
    divisors = []
    if not isPrime(value):
        if value % 2 == 0:
            divisors.append(2)
            value = value // 2
        i = 3
        while i <= value:
            if isPrime(value):
                divisors.append(value)
                break
            if value % i == 0:
                value = value // i
                if isPrime(i):
                    divisors.append(i)
            i += 2
    return divisors

def divisorsCount(value, divisors):
    div = divisors[:]
    divisors_count = {}
    while len(div) != 0:
        count = 0
        d = div.pop()
        while value%d == 0:
            value = value // d
            count += 1
        divisors_count[d] = count
    return divisors_count


def primeFactorization(value):
    div = divisors(value)
    divisor_count = divisorsCount(value, div)
    prime_string = ""
    for key in div:
        if divisor_count[key] > 0:
            temp_string = "("
            if divisor_count[key] > 1:
                temp_string += (str(key) + "**" + str(divisor_count[key]))
            else:
                temp_string += (str(key))
            temp_string += ")"
            prime_string += temp_string
    if len(prime_string) == 0:
        prime_string += ("(" + str(value) + ")")
    return prime_string

        
def main():
    while True:
        value = input("Prime factorization #")
        value = int(value)
        print(primeFactorization(value))
main()
