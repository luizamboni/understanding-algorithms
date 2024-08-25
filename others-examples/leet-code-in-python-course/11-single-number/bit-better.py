numbers = [4,4,2,2,3]

def single_number(numbers):
    return 2 * sum(set(numbers)) - sum(numbers)

print(
    single_number(numbers)
)