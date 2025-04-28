def numberOfBits(n):
    count = 0 
    while(n):
        count += 1
        n >>= 1 
    return count

n = int(input("Enter a number"))
binary_form = bin(n) [2:] # Convert to binary and remove '0b' prefix
print("Binary form:", binary_form)
print("Number of bits:", numberOfBits(n))