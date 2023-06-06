from math import sqrt, log10
count = 1
total = 0
while count <= 10**9: # Approaches pi squared over 6
    if not log10(count)%1:
        power = int(log10(count))
        print(f"10^{power} terms:", sqrt(6*total)) # prints logs of 1, 10, 100, 1000
    total += 1/(count**2)
    count += 1
print(sqrt(6*total)) # Manipulate to get pi