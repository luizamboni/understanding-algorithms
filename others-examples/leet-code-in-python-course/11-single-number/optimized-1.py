numbers = [4,4,2,2,1]

def single_number(numbers):
    single = 0
    for num in numbers:
        single ^= num
        print(num, single)
    return single
    

print(
    single_number(numbers)
)