import math
from itertools import combinations_with_replacement
        
def list_prime_between(a: int, b: int):
    assert a <= b, "b must greater than a"
    
    a = 2 if a <= 2 else a
    b = 2 if b <= 2 else b

    list_prime = [2] if (a <= 2) and (2 <= b) else []
    a = a + int(a%2 == 0)
    
    for num in range(a, b + 1, 2):
        if all(num%i!=0 for i in range(3,int(math.sqrt(num))+1, 2)):
            list_prime.append(num)
    
    return list_prime

        
def generator_prime_between(a: int, b: int):
    assert a <= b, "b must greater than a"
    
    a = 2 if a <= 2 else a
    b = 2 if b <= 2 else b

    if (a <= 2) and (2 <= b):
        yield 2

    a = a + int(a%2 == 0)
    
    for num in range(a, b + 1, 2):
        if all(num%i!=0 for i in range(3,int(math.sqrt(num))+1, 2)):
            yield num


def sumprimes(A, B):
    list_sum_prime = []
    for e in combinations_with_replacement(range(A, B + 1), 2):
        e1, e2 = e
        sum_e = sum(e)
        for p in generator_prime_between(sum_e + max(e), sum_e + B):
            e3 = p - sum_e
            list_sum_prime.append(tuple(sorted([e1, e2, e3])))

    return set(list_sum_prime)


if __name__ == "__main__":
    A = 3
    B = 20
    list_sum_prime = sumprimes(A, B)
    print(len(list_sum_prime))