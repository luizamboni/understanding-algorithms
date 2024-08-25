input = 13


def count_primes(input):

    if input <= 2:
        return 0

    count = 0
    
    for i in range(3, input+1):
        isPrime = True
        # testing division from 2 to next i
        # example: 
        ## input: 5 
        ## test division from 2 to 4 
        for j in range(2,i):
            if i % j == 0:
                isPrime = False
                break

        if isPrime:
            count += 1

    return count


print(
    count_primes(input)
)