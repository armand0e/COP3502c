def fibonacci(index):
    index -= 1
    sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
    if 0 <= index <= 19:
        return sequence[index]
    else:
        for i in range(index-19):
            next_num = sequence[-1] + sequence[-2]
            sequence.append(next_num)
        return sequence[index]
        
        
def is_prime(n):
    prime_marker = 0
    sqrtn = n**(1/2)
    if n > 1:
        for i in range(2, int(sqrtn) + 1):
            if (n % i == 0):
                prime_marker = 1
                break
        if (prime_marker == 0):
            return True
        else:
            return False
    else:
        return False
    

def print_prime_factors(n):
    ognum = n
    factors = []
    while n % 2 == 0:
        factors.append(int(2)),
        n = n / 2
         
    for i in range(3,int(n**(1/2))+1,2):
         
        while n % i== 0:
            factors.append(int(i)),
            n = n / i
             
    if n > 2:
        factors.append(int(n))
        
    iterations = 0
    factors_string = ""
    for i in range(len(factors)):
        iterations += 1
        factors_string += str(factors[i])
        if iterations != len(factors):
            factors_string += " * "
    print(f"{int(ognum)} = {factors_string}")
  


# TEST CASE 1
# print(fibonacci(1))
# print(fibonacci(2))
# print(fibonacci(3))
# print(fibonacci(6))
# print(fibonacci(25))
  
# TEST CASE 2
# print(is_prime(2))
# print(is_prime(11))  
# print(is_prime(1741))  
# print(is_prime(1))  
# print(is_prime(9))  
# print(is_prime(-2))

# TEST CASE 3
print_prime_factors(10)
print_prime_factors(2)
print_prime_factors(24)
print_prime_factors(2475)
print_prime_factors(23)

