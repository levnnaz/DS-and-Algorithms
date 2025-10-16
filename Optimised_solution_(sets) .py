# Nazar Levchuk, ID:001408115, Date 28/02/2025
# Optimised solution using set() data structure
import time

# function to check for prime numbers
def find_primes(n):
    if n < 2:
        return False
    if n in (2, 3):  #return 2 and 3 directly
        return True
    if n % 2 == 0 or n % 3 == 0:  # false for multiple of 2 and 3
        return False
    # 6k ± 1 rule for checking
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
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
            decimals = (decimals << 1) | int(binary_str[j]) #converting to decimals
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

    # convert to string and sort primes
    primes_strings = sorted(map(str, primes), key=int)
    len_primes = len(primes_strings)

    # if-else to print output
    if len_primes < 6:
        print(f"{len(primes)}: {', '.join(primes_strings)}")
    else:
        print(f"{len(primes)}: {', '.join(primes_strings[:3] + primes_strings[-3:])}")

# test cases
test_cases = [
    ("0100001101001111", 999999),       #Time taken: 0.00008273124694824219
    ("01000011010011110100110101010000", 999999),    #Time taken: 0.00018310546875
    ("1111111111111111111111111111111111111111", 999999),      #Time taken: 0.0001583099365234375
    ("010000110100111101001101010100000011000100111000", 999999999),    #Time taken: 0.0007810592651367188
    ("01000011010011110100110101010000001100010011100000110001", 123456789012),    #Time taken: 0.004132986068725586
    ("0100001101001111010011010101000000110001001110000011000100111001", 123456789012345),      #Time taken:    0.2313861846923828
    ("010000110100111101001101010100000011000100111000001100010011100100100001", 123456789012345678),       #Time taken: 4.834602117538452
    ("01000011010011110100110101010000001100010011100000110001001110010010000101000001", 1234567890123456789),      #Time taken: 6.371043920516968
    ("0100001101001111010011010101000000110001001110000011000100111001001000010100000101000100", 1234567890123456789),      #Time taken: 16.45944595336914
    ("010000110100111101001101010100000011000100111000001100010011100100100001010000010100010001010011", 12345678901234567890)      #Time taken: 22.000739097595215
]


# for loop to run test cases
for binary_string, num in test_cases:
    start = time.time()
    prime_nums = get_primes(binary_string, num)
    get_printed(prime_nums)
    end = time.time()
    print(end - start, "\n")

