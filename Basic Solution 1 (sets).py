# Nazar Levchuk, ID:001408115, Date 15/02/2025
#Basic solution using set() data structure
import time

# function to check for prime numbers
def find_primes(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) +1):
        if n % i == 0:
            return False
    return True

# main func that extracts substrings and get primes
def get_primes(binary_str, num):

    if set(binary_str) - {'0', '1'}:  # checking for valid input
        return set() #returning empty set

    #sets to store the data
    prime_numbers = set()
    decimal_nums = set()
    #len of input string
    n = len(binary_str)

    #for loops convert to decimals
    for i in range(n):
        decimals = 0  #assigning decimals to 0
        for j in range(i, n):
            decimals = decimals * 2 + int(binary_str[j]) #converting to decimals
            if decimals >= num:
                break
            decimal_nums.add(decimals) #add decimals to the set of decimals
    #for loop to check for primes
    for dec in decimal_nums:
        if find_primes(dec):
            prime_numbers.add(dec) #adding prime numbers to the set

    return prime_numbers #returning prime nums

# function to print output
def get_printed(primes):

    if len(primes) == 0 :
        print("0: Invalid binary string")
        return

    len_primes = len(primes)
    primes_strings = set() #creating set to store strings
    #for loop to add strings
    for num in primes:
        primes_strings.add(str(num))
    sorted_strings = sorted(primes_strings, key=int) #sorting strings

    # if-else to print output
    if len_primes < 6:
        print(f"{len(primes)}: {', '.join(sorted_strings)}")
    else:
        print(f"{len(primes)}: {', '.join(sorted_strings[:3] + sorted_strings[-3:])}")

# test cases
test_cases = [
    ("0100001101001111", 999999),       #Time taken: 8.7738037109375e-05
    ("01000011010011110100110101010000", 999999),    #Time taken: 0.00024175643920898438
    ("1111111111111111111111111111111111111111", 999999),      #Time taken: 0.0001690387725830078
    ("010000110100111101001101010100000011000100111000", 999999999),    #Time taken: 0.001767873764038086
    ("01000011010011110100110101010000001100010011100000110001", 123456789012),    #Time taken: 0.011990070343017578
    ("0100001101001111010011010101000000110001001110000011000100111001", 123456789012345),      #Time taken:    0.6700890064239502
    ("010000110100111101001101010100000011000100111000001100010011100100100001", 123456789012345678),       #Time taken: 15.323393106460571
    ("01000011010011110100110101010000001100010011100000110001001110010010000101000001", 1234567890123456789),      #Time taken: 21.74988317489624
    ("0100001101001111010011010101000000110001001110000011000100111001001000010100000101000100", 1234567890123456789),      #Time taken: 53.466941118240356
    ("010000110100111101001101010100000011000100111000001100010011100100100001010000010100010001010011", 12345678901234567890)      #Time taken: More than 60 sec
]

# for loop to run test cases
for binary_string, num in test_cases:
    start = time.time()
    prime_nums = get_primes(binary_string, num)
    get_printed(prime_nums)
    end = time.time()
    print(end - start, "\n")





