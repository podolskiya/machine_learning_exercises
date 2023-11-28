# Function
def prime_finder(n):
    prime_numbers = []
    for num in range(2, n + 1):
        prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime = False
                break
        if prime and num > 1:
            prime_numbers.append(num)
    return prime_numbers

# Test the function
result = prime_finder(27)
print(result)  
# Output: [2, 3, 5, 7, 11, 13, 17, 19, 23]
