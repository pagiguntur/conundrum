def largest_factor(x:int) -> int:
    prime = 1
    largest = 2
    listPrime = [2,3,5,7]
    while prime < x:
        for i in range(2, prime):
            if prime%i != 0 and x%prime == 0:
                largest = prime
        prime += 1
    return largest

print(largest_factor(7))