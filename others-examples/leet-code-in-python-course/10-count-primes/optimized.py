from math import ceil, sqrt

def count_primes(n: int) -> int:		
        
    if n < 2:
        return 0
    
    isPrime = [True] * n
    isPrime[0] = isPrime[1] = False
    
    for i in range(2, ceil(sqrt(n))):
        if isPrime[i]:
            for multiples_of_i in range(i * i, n, i):
                isPrime[multiples_of_i] = False
    
    return sum(isPrime)


input = 13
print(
    count_primes(input)
)