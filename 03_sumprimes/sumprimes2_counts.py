import math

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
            
            
def count_k1k2k3(sum_k, max_k):
    start_1 = max(sum_k - 2*max_k, 1)
    end_1 = min(sum_k//3, max_k)
    
    count = 0
    for k1 in range(start_1, end_1 + 1):
        
        start_2 = max(sum_k - k1 - max_k, k1)
        end_2 = min((sum_k - k1)//2, max_k)

        count_k23 = end_2 - start_2 + 1
        count += count_k23
    
    return count
    
    
def count_x1x2x3(sum_x, min_x, max_x):
    sum_k = sum_x - 3*(min_x - 1)
    max_k = max_x - min_x + 1
    
    count = count_k1k2k3(sum_k, max_k)
    
    return count
    
    
def sumprimes_count(A, B):
    counts = 0
    for p in generator_prime_between(3*A, 3*B):
        count = count_x1x2x3(p, A, B)
        counts += count
    return counts
    
    
if __name__ == "__main__":
    A, B = list(map(int, input().split(" ")))
    counts = sumprimes_count(A, B)
    print(counts)
