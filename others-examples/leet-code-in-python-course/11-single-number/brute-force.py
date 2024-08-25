numbers = [4,4,2,2,3]

def single_number(numbers):
    numbers_occurrence = {}

    for n in numbers:
        if n in numbers_occurrence:
            numbers_occurrence[n] += 1
        else:
            numbers_occurrence[n] = 1

        
    for n in numbers_occurrence:
        if numbers_occurrence[n] == 1:
            return n

print(
    single_number(numbers)
)