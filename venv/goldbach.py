def goldbach_conj(number):
    x, y = 0, 0
    result = 0
    if not number % 2:
        prime_list = list[number]
        while result != number:
            for i in range(len(prime_list)):
                x = prime_list[i]
                if result == number: break
                for j in range(len(prime_list)):
                    y = prime_list[j]
                    result = x + y
                    print("Adding {} and {}.".format(x, y))
                    print("Result is {}".format(result))
                    if result == number:
                        break
    return x, y

goldbach_conj(4)