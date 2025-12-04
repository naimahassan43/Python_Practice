# function that returns prime numbers of a given range
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def prime_numbers_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes
# Example usage
if __name__ == "__main__":
    start_range = 1
    end_range = 50
    primes = prime_numbers_in_range(start_range, end_range)
    print(f"Prime numbers between {start_range} and {end_range}: {primes}")# This is a sample Python script.
