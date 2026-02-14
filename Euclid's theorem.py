# Euclid's proof 
primenumber = [] # prime numbers
solution = [] 
for i in range(5):
    primenumber.append(int(input("Enter a prime number:")))

number = primenumber[0] * primenumber[1] * primenumber[2] * primenumber[3] * primenumber[4] 

solution = number + 1

# The resulting variable, which we call a number, is the product of the entered prime numbers plus one.
if solution in primenumber:
    print("The number is a prime number")

else:
    print("The number itself is not a prime number, but it has a new prime number among its factors.")

print("THERE ARE INFINITE PRIME NUMBERS!")

# In both cases, there is a new prime number.
# THERE ARE INFINITE PRIME NUMBERS!
